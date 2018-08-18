# quantiles.py
import click
import math

def quantile(population, nquantile):
	print("Population: ", population, " nQuantile: ", nquantile)
	population_size = len(population)
	quantiles=[]
	for member in range(1, nquantile):
		quantiles.append(population[math.ceil(population_size*(member/nquantile))-1])
	return quantiles

@click.command()
@click.argument(
	'input_file',
	type=click.File('rb'),
)
def main(input_file):
	"""Reads the input: All population members sep by newline. n-quantile, newline.
	Then, ouputs the n-quantiles
	"""
	input_data = []
	for line in input_file:
		input_data.append(int(line.strip()))
	population = input_data[0:len(input_data)-1]
	population.sort()
	nquantile = input_data[len(input_data)-1]
	click.echo(quantile(population, nquantile))

if __name__ == "__main__":
	main()
