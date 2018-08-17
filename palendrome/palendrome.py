# palendrome.py
import click

def is_palendrome(possible_palendrome):
	possible_palendrome_length = len(possible_palendrome)
	for index in range(possible_palendrome_length//2):		# // rounds to floor
		if possible_palendrome[index] != possible_palendrome[(possible_palendrome_length-index)-1]:
			return False
	return True

@click.command()
@click.argument(
	'input_file',
	type=click.File('rb'),
)
def main(input_file):
	"""Prints true if the input is palendromatic

	Either specify a filename or give stdin e.g. echo "blablalbalb" | ./virtualenv/palendrome/bin/python ./palendrome.py -
	"""
	click.echo(is_palendrome(input_file.read().strip()))

if __name__ == "__main__":
	main()
