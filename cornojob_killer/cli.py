from abstra.cli import CLI
import tempfile


"""
If you're reading this, you're really paranoid about safety, right?

Although this is a joke, we take security extremely seriously. 
Abstra is the safest and fastest way to automate your company's processes.

We're not kidding about that.

Want to know more? Contact us at help@abstra.io
"""
def main():
    print("So you're a corno? Your secret is safe with us. ¯\\_(ツ)_/¯")
    print("Welcome to cornojob-killer - the only weapon you'll ever need to destroy annoying, repetitive tasks.")
    print("For serious use cases, use the `abstra` CLI")
    input("Ready to kill your corno jobs?")
    print("Abstra will start in a temporary directory. Changes will not be saved.")
    print("For serious use cases, use the `abstra` CLI")
    print("Read the docs at docs.abstra.io")
    temp_dir = tempfile.mkdtemp()
    cli = CLI()
    cli.serve(temp_dir)


if __name__ == '__main__':
    main()

