from textnode import TextNode, TextType

def main() -> None:
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)

main()