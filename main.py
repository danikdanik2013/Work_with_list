#utf-8 python 3.6
import itertools
import time


def main():
	new_list = []
	name = []
	def names():
		while True:
			name_inputs = input('Enter name convicted: ')
			name.append(name_inputs)
			more_names = input('Do you want to add more name?(Yes or No) ')
			if more_names == 'No' or more_names == 'no':
				break
			elif more_names == 'Yes' or more_names == 'yes':
				continue
			else:
				print('We deleted last name. Try again!')
				del name[-1]
		return name
	names()
	
	def list(name, new_list):
		list_all = input('Do u want to check all names?:  ')

		if list_all == 'yes' or list_all == 'Y' or list_all == 'Yes':
			print(name)

		while True:

			question = input('Enter ONE name for kill: ')

			if question in name:
				print( '%s, вы обвиненные в государственной измене' % (question))
				print('За это вас следует расстрелять')
				it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
				for x in range(30):
					time.sleep(.3)
					print(next(it), end='', flush=True)
				enter = name.index(question)
				del name[enter]
				print('\nKilled.')
			

				print(name)
			else:
				print('sorry, check your name')
				error_more = input('want again? ')
				if error_more == 'yes' or more == 'Yes':
					continue
				else:
					break

			more = input('Do u want more? ')
			if more == 'yes' or more == 'yes':
				continue
			else:
				break

	list(name, new_list)
	


if __name__ == '__main__':
    main()
