import argparse
import taskTracker as tt

def main():
    parser = argparse.ArgumentParser(description="A simple Todo list CLI application")
    parser.add_argument("add", type=str, help="Task name")

    args = parser.parse_args()

    tt.add_task(args.add)

if __name__ == "__main__":
    main()