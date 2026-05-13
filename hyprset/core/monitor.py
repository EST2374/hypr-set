import json
import re
import subprocess

import hyprset.config as app_config

# TODOS
# Enable/Disable
# MONITOR POS

ROTATIONS: dict[str, str] = {
    "Normal": "0",
    "90°": "1",
    "180°": "2",
    "270°": "3",
    "flipped": "4",
    "flipped + 90°": "5",
    "flipped + 180°": "6",
    "flipped + 270°": "7",
}

BLOCK_PATTERN = re.compile(r"hl\.monitor\(\{(.*?)\}\)", re.DOTALL)
FIELD_PATTERN = re.compile(r'(\w+)\s*=\s*(".*?"|[\d.]+|true|false)')


def _parse_fields(block_content: str) -> dict:
    return {
        m.group(1): m.group(2).strip('"') for m in FIELD_PATTERN.finditer(block_content)
    }


def _build_monitor_block(fields: dict) -> str:
    lines = []
    for key, value in fields.items():
        if re.match(r"^[\d.]+$", value) or value in ("true", "false"):
            lines.append(f"    {key} = {value},")
        else:
            lines.append(f'    {key} = "{value}",')
    return "hl.monitor({\n" + "\n".join(lines) + "\n})"


def get_monitor_data() -> list | None:
    try:
        result = subprocess.run(
            ["hyprctl", "monitors", "-j"],
            capture_output=True,
            text=True,
            check=True,
        )
        return json.loads(result.stdout)
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        print(f"An error occurred: {e}")
        return None


def get_monitor_names() -> list[str]:
    data = get_monitor_data()
    if data is None:
        return []
    return [monitor["name"] for monitor in data]


def get_monitor_resolution(mon_index: int) -> list[str]:
    data = get_monitor_data()
    if data is None:
        return []
    try:
        return data[mon_index]["availableModes"]
    except (IndexError, KeyError) as e:
        print(f"Error fetching modes: {e}")
        return []


def get_monitor_count() -> int:
    data = get_monitor_data()
    return len(data) if data is not None else 0


def set_default_monitors_in_config():
    data = get_monitor_data()
    if data is None:
        return

    try:
        with open(app_config.CONFIG_FILE, "r") as f:
            content = f.read()

        existing = {
            _parse_fields(block.group(1)).get("output", "")
            for block in BLOCK_PATTERN.finditer(content)
        }

        new_blocks = []
        for monitor in data:
            name = monitor["name"]
            if name not in existing and "" not in existing:
                new_blocks.append(
                    _build_monitor_block(
                        {
                            "output": name,
                            "mode": "preferred",
                            "position": "auto",
                            "scale": "1.0",
                            "transform": "0",
                        }
                    )
                )

        if new_blocks:
            content += "\n\n" + "\n\n".join(new_blocks) + "\n"
            with open(app_config.CONFIG_FILE, "w") as f:
                f.write(content)

    except OSError as e:
        print(f"Error writing config: {e}")


def apply_monitor_settings(
    mon_name, mon_res, mon_pos, mon_scale, mon_mirror, mon_rotation
):
    new_rotation = ROTATIONS[mon_rotation]

    with open(app_config.CONFIG_FILE, "r") as f:
        content = f.read()

    all_matches = list(BLOCK_PATTERN.finditer(content))

    target_index = None
    for i, block_match in enumerate(all_matches):
        fields = _parse_fields(block_match.group(1))
        output_val = fields.get("output", "")
        if output_val == mon_name or output_val == "":
            target_index = i
            break

    if target_index is not None:
        fields = _parse_fields(all_matches[target_index].group(1))
    else:
        fields = {}

    fields["output"] = mon_name
    fields["mode"] = mon_res
    fields["position"] = mon_pos
    fields["scale"] = str(mon_scale)
    fields["transform"] = new_rotation
    if mon_mirror != "None":
        fields["mirror"] = mon_mirror
    else:
        fields.pop("mirror", None)

    new_block = _build_monitor_block(fields)

    if target_index is not None:
        result = content
        offset = 0
        for i, m in enumerate(all_matches):
            start = m.start() + offset
            end = m.end() + offset
            replacement = new_block if i == target_index else ""
            result = result[:start] + replacement + result[end:]
            offset += len(replacement) - (m.end() - m.start())
        clean_content = result
    else:
        clean_content = content.rstrip() + "\n\n" + new_block + "\n"

    with open(app_config.CONFIG_FILE, "w") as f:
        f.write(clean_content)


def set_default_monitors_button():
    data = get_monitor_data()
    if data is None:
        return
    try:
        with open(app_config.CONFIG_FILE, "r") as f:
            content = f.read()

        all_matches = list(BLOCK_PATTERN.finditer(content))

        new_blocks = []
        for i, block_match in enumerate(all_matches):
            fields = _parse_fields(block_match.group(1))
            output_val = fields.get("output", "")
            monitor = next(
                (m for m in data if m["name"] == output_val),
                data[i] if i < len(data) else None,
            )
            if monitor is None:
                new_blocks.append("")
            else:
                new_blocks.append(
                    _build_monitor_block(
                        {
                            "output": monitor["name"],
                            "mode": "preferred",
                            "position": "auto",
                            "scale": "1.0",
                            "transform": "0",
                        }
                    )
                )

        result = content
        offset = 0
        for i, m in enumerate(all_matches):
            start = m.start() + offset
            end = m.end() + offset
            replacement = new_blocks[i]
            result = result[:start] + replacement + result[end:]
            offset += len(replacement) - (m.end() - m.start())

        existing_outputs = {
            _parse_fields(m.group(1)).get("output", "") for m in all_matches
        }
        appended = []
        for monitor in data:
            if monitor["name"] not in existing_outputs and "" not in existing_outputs:
                appended.append(
                    _build_monitor_block(
                        {
                            "output": monitor["name"],
                            "mode": "preferred",
                            "position": "auto",
                            "scale": "1.0",
                            "transform": "0",
                        }
                    )
                )
        if appended:
            result = result.rstrip() + "\n\n" + "\n\n".join(appended) + "\n"

        with open(app_config.CONFIG_FILE, "w") as f:
            f.write(result)

    except OSError as e:
        print(f"Error writing config: {e}")


def get_cur_rotation(mon_name: str) -> str:
    try:
        with open(app_config.CONFIG_FILE, "r") as f:
            content = f.read()
    except FileNotFoundError:
        return "Normal"

    for block in BLOCK_PATTERN.finditer(content):
        fields = _parse_fields(block.group(1))
        output_val = fields.get("output", "")
        if output_val == mon_name or output_val == "":
            code = fields.get("transform", "0")
            return next((name for name, c in ROTATIONS.items() if c == code), "Normal")

    return "Normal"
