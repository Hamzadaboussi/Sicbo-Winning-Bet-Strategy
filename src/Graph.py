import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


def showGraph(repeated_data):
    plt.figure(figsize=(12, 6))

    plt.plot(repeated_data['time'], repeated_data['balance'], color='blue', marker='o', label='Balance')

    plt.plot(repeated_data['time'], repeated_data['profits'], color='red', marker='o', label='Profits')
    plt.xlabel('Time')
    plt.ylabel('Balance')
    plt.title('Balance Over Time')
    plt.legend()
    plt.show()
