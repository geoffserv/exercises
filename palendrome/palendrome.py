# palendrome.py
import click

def is_acronym(possible_acronym):
	possible_acronym_length = len(possible_acronym)
	for index in range(possible_acronym_length//2):		# // rounds to floor
		if possible_acronym[index] != possible_acronym[(possible_acronym_length-index)-1]:
			return False
	return True

@click.command()
@click.argument(
	'possible_acronym',
)
def main(possible_acronym):
	print(is_acronym(possible_acronym))

if __name__ == "__main__":
	main()
