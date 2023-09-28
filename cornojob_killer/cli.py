from abstra.cli import CLI
import tempfile, time, requests, uuid, hashlib, threading


def count():
    """
    Counting function to measure the number of times this lib was used.
    """

    sha256_hash = hashlib.sha256()
    sha256_hash.update(str(uuid.getnode()).encode("utf-8"))
    hashed_string = sha256_hash.hexdigest()
    requests.get(
        "https://cornojob-killer.abstra.app/_hooks/count",
        headers={
            "counter": hashed_string  # We don't want to know who you are, we just want to know how many people are using this. :)
        },
    )


"""
If you're reading this, you're really paranoid about safety, right?

Although this is a joke, we take security extremely seriously. 
Abstra is the safest and fastest way to automate your company's processes.

We're not kidding about that.

Want to know more? Contact us at help@abstra.io
"""


def main():
    threading.Thread(target=count).start()
    print(
        "Welcome to cornojob-killer - the only weapon you'll ever need to destroy annoying, repetitive tasks."
    )
    input("Ready to kill your corno jobs?\nPress enter to continue.")
    print("Abstra will start in a temporary directory. Changes will not be saved.")
    print("\nFor serious use cases, use the `abstra` CLI")
    print("Read the docs at docs.abstra.io")
    time.sleep(2)
    temp_dir = tempfile.mkdtemp()
    cli = CLI()
    cli.serve(temp_dir)


if __name__ == "__main__":
    main()
