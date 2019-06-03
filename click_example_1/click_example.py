import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()

"""
Example 1:

dinesh@dinesh-VirtualBox:~/Desktop/click$ python3 click_example.py --help
Usage: click_example.py [OPTIONS]

  Simple program that greets NAME for a total of COUNT times.

Options:
  --count INTEGER  Number of greetings.
  --name TEXT      The person to greet.
  --help           Show this message and exit.

Example 2:

dinesh@dinesh-VirtualBox:~/Desktop/click$ python3 click_example.py
Your name: Dinesh
Hello Dinesh!

Example 3:

dinesh@dinesh-VirtualBox:~/Desktop/click$ python3 click_example.py --count=3 --name Dinesh
Hello Dinesh!
Hello Dinesh!
Hello Dinesh!

"""
