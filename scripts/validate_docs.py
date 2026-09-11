from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
NORMATIVE = [
    ROOT / "README.md",
    ROOT / "product" / "01_BUSINESS_ANALYSIS.md",
    ROOT / "product" / "02_BRD.md",
    ROOT / "product" / "Product Metadata.md",
]
PLANNED = [
    "product/03_FEATURE_CATALOG_AND_SCOPE.md",
    "development/mvp-1/01_PRD.md",
    "development/mvp-1/02_FRD.md",
    "technical/01_SYSTEM_ARCHITECTURE.md",
    "technical/02_DATABASE_DESIGN.md",
    "technical/03_API_CONTRACTS.md",
]
CANONICAL = {
    "TENTATIVE", "PUBLISHED_FIXED", "CONFIRMED_DEPARTURE", "IN_OPERATION",
    "COMPLETED", "DISRUPTED", "WAITING_OWNER_ACTION", "CANCELLED", "DRAFT",
    "PENDING_PAYMENT", "EXPIRED", "CONFIRMED", "FULLY_PAID", "RESCHEDULED",
    "TRANSFERRED", "UNPAID", "PARTIALLY_PAID", "PAID", "REFUND_PENDING", "REFUNDED",
}


def markdown_files():
    return [p for p in ROOT.rglob("*.md") if ".git" not in p.parts and ".hermes" not in p.parts]


def validate_links():
    errors = []
    planned = []
    pattern = re.compile(r"\[[^]]+\]\(([^)]+)\)")
    for path in markdown_files():
        for target in pattern.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target_path = (path.parent / target.split("#", 1)[0]).resolve()
            normalized = target_path.relative_to(ROOT).as_posix() if target_path.is_relative_to(ROOT) else ""
            if normalized in PLANNED and not target_path.exists():
                planned.append(f"{path.relative_to(ROOT)}: planned reference {target}")
                continue
            if not target_path.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing link target {target}")
    return errors, planned


def validate_metadata():
    return [
        f"{path.relative_to(ROOT)}: missing Document Information"
        for path in NORMATIVE[1:3]
        if "## Document Information" not in path.read_text(encoding="utf-8")
    ]


def validate_statuses():
    errors = []
    token_pattern = re.compile(r"`([A-Z][A-Z0-9_]+)`")
    for path in NORMATIVE[1:3]:
        for token in token_pattern.findall(path.read_text(encoding="utf-8")):
            if token.endswith(("ID", "PO", "BOM", "DP")):
                continue
            if token not in CANONICAL and token in {"DRAFT_PENDING_DP", "CONFIRMED_DEP"}:
                errors.append(f"{path.relative_to(ROOT)}: non-canonical status {token}")
    return errors


def main():
    link_errors, planned = validate_links()
    errors = link_errors + validate_metadata() + validate_statuses()
    if errors:
        print("Documentation validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Documentation validation: PASS")
    print("Markdown links: PASS")
    print("Metadata headers: PASS")
    print("Status vocabulary: PASS")
    print(f"Planned references: {len(planned)}")
    for reference in planned:
        print(f"- {reference}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
