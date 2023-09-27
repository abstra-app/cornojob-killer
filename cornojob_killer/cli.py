from abstra.cli import CLI
import tempfile, time


"""
If you're reading this, you're really paranoid about safety, right?

Although this is a joke, we take security extremely seriously. 
Abstra is the safest and fastest way to automate your company's processes.

We're not kidding about that.

Want to know more? Contact us at help@abstra.io
"""
def main():
    print("Welcome to cornojob-killer - the only weapon you'll ever need to destroy annoying, repetitive tasks.")
    input("Ready to kill your corno jobs?")
    print("Abstra will start in a temporary directory. Changes will not be saved.")
    print("\nFor serious use cases, use the `abstra` CLI")
    print("Read the docs at docs.abstra.io")
    time.sleep(2)
    temp_dir = tempfile.mkdtemp()
    cli = CLI()
    cli.serve(temp_dir)


if __name__ == '__main__':
    main()

