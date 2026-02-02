def group_item_blocks(lines: list[str]) -> list[list[str]]:
    blocks = []
    current = []

    for line in lines:
        # 상품 번호로 시작하면 새 블록
        if line[:3].isdigit():
            if current:
                blocks.append(current)
            current = [line]
        else:
            if current:
                current.append(line)

    if current:
        blocks.append(current)

    return blocks
