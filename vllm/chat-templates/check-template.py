import argparse
from jinja2 import Template


def main():
    args = get_args()
    # print(args)

    with open(args.chat_template[0]) as f:
        template = Template(f.read())

    messages = [
        {"role": "system", "content": "あなたは誠実で優秀な日本人のアシスタントです。"},
        {"role": "user", "content": "東京の観光名所を教えて下さい。"},
        # {"role": "assistant", "content": "東京タワーがオススメです。"},
        # {"role": "user", "content": "大阪の観光名所を教えて下さい。"},
    ]

    result = template.render(messages=messages, add_generation_prompt=True)
    print(result)


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--chat-template", nargs=1, required=True, help="Specify chat template.")

    return parser.parse_args()


if __name__ == "__main__":
    main()
