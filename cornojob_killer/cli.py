from abstra.cli import CLI
import tempfile


"""
If you're reading this, you're really paranoic with safety, right?

Even though this is a joke, we take security very seriously.
Abstra is the safest and fastest way to automate your company's processes.

We're not kidding.

Want to know more? Contact us at help@abstra.io
"""
def main():
    print("TODO: Funny message")
    print("For serious use cases, use the `abstra` CLI")
    input()
    print("Abstra will start in a temporary directory")
    print("For serious use cases, use the `abstra` CLI")
    print("Read the docs at docs.abstra.io")
    temp_dir = tempfile.mkdtemp()
    cli = CLI()
    cli.serve(temp_dir)


if __name__ == '__main__':
    main()

