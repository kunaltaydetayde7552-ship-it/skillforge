import sys, os, re, pathlib


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return None, "missing or malformed YAML frontmatter"
    body = m.group(1)
    fields = dict(re.findall(r"^(\w+):\s*(.+)$", body, re.M))
    return fields, None


REQUIRED = ["name", "trigger"]


def validate_skill(path):
    errors = []
    text = pathlib.Path(path).read_text(encoding="utf-8")
    fields, err = parse_frontmatter(text)
    if err:
        return [err]
    for key in REQUIRED:
        if key not in fields:
            errors.append(f"missing required field: {key}")
    for ref in re.findall(r"`([\w./-]+\.\w+)`", text):
        if "/" in ref and not os.path.exists(
            os.path.join(os.path.dirname(path), ref)
        ):
            errors.append(f"referenced file does not exist: {ref}")
    return errors


def main():
    target = sys.argv[2] if len(sys.argv) > 2 else "skills"
    total, failed = 0, 0
    for skill in pathlib.Path(target).rglob("SKILL.md"):
        total += 1
        errs = validate_skill(skill)
        if errs:
            failed += 1
            print(f"FAIL {skill}")
            for e in errs:
                print(f"   - {e}")
        else:
            print(f"OK   {skill}")
    print(f"\n{total - failed}/{total} skills valid")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
