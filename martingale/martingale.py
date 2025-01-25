""""""  		  	   		 	 	 			  		 			     			  	 
"""Assess a betting strategy.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	 	 			  		 			     			  	 
Atlanta, Georgia 30332  		  	   		 	 	 			  		 			     			  	 
All Rights Reserved  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Template code for CS 4646/7646  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	 	 			  		 			     			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		 	 	 			  		 			     			  	 
and other users of this template code are advised not to share it with others  		  	   		 	 	 			  		 			     			  	 
or to make it available on publicly viewable websites including repositories  		  	   		 	 	 			  		 			     			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	 	 			  		 			     			  	 
or edited.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
We do grant permission to share solutions privately with non-students such  		  	   		 	 	 			  		 			     			  	 
as potential employers. However, sharing with other current or future  		  	   		 	 	 			  		 			     			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	 	 			  		 			     			  	 
GT honor code violation.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
-----do not edit anything above this line---  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Student Name: Tucker Balch (replace with your name)  		  	   		 	 	 			  		 			     			  	 
GT User ID: tb34 (replace with your User ID)  		  	   		 	 	 			  		 			     			  	 
GT ID: 900897987 (replace with your GT ID)  		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
import numpy as np  		  	   		 	 	 			  		 			     			  	 
import matplotlib.pyplot as plt  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def author():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    :return: The GT username of the student  		  	   		 	 	 			  		 			     			  	 
    :rtype: str  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    return "jtang414"  # replace tb34 with your Georgia Tech username.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def gtid():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    :return: The GT ID of the student  		  	   		 	 	 			  		 			     			  	 
    :rtype: int  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    return 904051319  # replace with your GT ID number  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def get_spin_result(win_prob):  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
    :param win_prob: The probability of winning  		  	   		 	 	 			  		 			     			  	 
    :type win_prob: float  		  	   		 	 	 			  		 			     			  	 
    :return: The result of the spin.  		  	   		 	 	 			  		 			     			  	 
    :rtype: bool  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    result = False  		  	   		 	 	 			  		 			     			  	 
    if np.random.random() <= win_prob:  		  	   		 	 	 			  		 			     			  	 
        result = True  		  	   		 	 	 			  		 			     			  	 
    return result  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	
def experiment_1(
        num_episodes
        ,num_bets
        ,win_prob
        ):


    bet_stats = (
        num_episodes
        ,num_bets + 1
        )

    episode_winnings = np.zeros(bet_stats)

    # Simulate episodes
    for i in range(num_episodes):
        episode_winnings[i][0] = 0
        bet_count = 1

        while bet_count < num_bets + 1:
            if episode_winnings[i][bet_count - 1] >= 80:
                episode_winnings[i][bet_count:] = 80  # Set all future values to 80
                break  # End early as target has been reached
            
            bet_amount = 1
            won = False

            while not won and bet_count < num_bets:
                won = get_spin_result(win_prob)

                if won:
                    episode_winnings[i][bet_count] = episode_winnings[i][bet_count - 1] + bet_amount
                else:
                    episode_winnings[i][bet_count] = episode_winnings[i][bet_count - 1] - bet_amount
                    bet_amount *= 2

                bet_count += 1

    # Transpose for easier analysis
    return episode_winnings.transpose()


def experiment_2(
        num_episodes
        ,num_bets
        ,win_prob
        ):

    bet_stats = (
        num_episodes
        ,num_bets + 1
        )

    episode_winnings = np.full(
        bet_stats
        ,256
        )

    for i in range(num_episodes):
        bet_count = 1
        while episode_winnings[i, bet_count - 1] > 0 and \
              episode_winnings[i, bet_count - 1] < 80 + 256 and bet_count < bet_stats[1]:
            bet_amount = 1
            won = False
            
            while not won and bet_count < bet_stats[1]:
                won = get_spin_result(win_prob)  # simulate spin result

                # Update the winnings based on the outcome
                if won:
                    episode_winnings[i, bet_count] = episode_winnings[i, bet_count - 1] + bet_amount
                else:
                    episode_winnings[i, bet_count] = episode_winnings[i, bet_count - 1] - bet_amount
                    bet_amount = min(bet_amount * 2, episode_winnings[i, bet_count] - 1)  # double the bet or bet remaining funds

                bet_count += 1

        # Carry forward the result if we have reached an end condition (bankrupt or goal reached)
        final_winnings = episode_winnings[i, bet_count - 1]
        if final_winnings >= 80 + 256:
            episode_winnings[i, bet_count:] = 80 + 256
        elif final_winnings <= 0:
            episode_winnings[i, bet_count:] = 0

    return episode_winnings.transpose() - 256


def test_code():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    Method to test your code  		  	   		 	 	 			  		 			     			  	 
    """	   		 	 	 			  		 			     			  	 
    win_prob = 0.4737  # win prob based on the wiki  		  	   		 	 	 			  		 			     			  	 
    np.random.seed(gtid())  # do this only once  		  	   		 	 	 			  		 			     			  	 
    print(get_spin_result(win_prob))  # test the roulette spin  		  	   		 	 	 			  		 			     			  	 
    # add your code here to implement the experiments  		  	   		 	 	 			  		 			     			  	 

    
    # Figure 1.
    num_episodes = 10
    num_successive_bets = 1000
    winnings = experiment_1(
        num_episodes
        ,num_successive_bets
        ,win_prob
        )
    
    plt.figure(1)
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.plot(winnings)
    plt.xlabel("Successive Bets")
    plt.ylabel("Winnings ($)")
    plt.title("Roulette Simulation - Episode Winnings")
    plt.legend([str(i) for i in range(1, num_episodes + 1)])
    plt.grid()
    plt.show()
    plt.savefig("Figure_1") 


    # Figure 2.
    num_episodes = 1000
    num_successive_bets = 1000
    winnings = experiment_1(
        num_episodes
        ,num_successive_bets
        ,win_prob
        )

    mean_winnings = np.zeros(
        (
            num_successive_bets + 1
            ,1
            )
            )
    std_winnings = np.zeros(
        (
            num_successive_bets + 1
            ,1
            )
        )
    
    for i in range(1, num_successive_bets + 1):
        mean_winnings[i] = np.mean(winnings[i])
        std_winnings[i] = np.std(winnings[i])

    data = np.concatenate(
        (
            mean_winnings + std_winnings
            ,mean_winnings
            ,mean_winnings -std_winnings
            )
            ,axis=1
            )
    
    plt.figure(2)
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.plot(data)
    plt.legend(["Upper", "Mean", "Lower"])
    plt.xlabel("Successive Bets")
    plt.ylabel("Winnings ($)")
    plt.title("Roulette Simulation - Mean Winnings")
    plt.show()
    plt.savefig("Figure_2") 



    # Figure 3.
    num_episodes = 1000
    num_successive_bets = 1000
    winnings = experiment_1(
        num_episodes
        ,num_successive_bets
        ,win_prob
        )

    median_winnings = np.zeros(
        (
            num_successive_bets + 1
            ,1
            )
            )
    std_winnings = np.zeros(
        (
            num_successive_bets + 1
            ,1
            )
        )
    
    for i in range(1, num_successive_bets + 1):
        median_winnings[i] = np.median(winnings[i])
        std_winnings[i] = np.std(winnings[i])

    data = np.concatenate(
        (
            median_winnings + std_winnings
            ,median_winnings
            ,median_winnings -std_winnings
            )
            ,axis=1
            )

    plt.figure(3)
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.plot(data)
    plt.legend(["Upper", "Median", "Lower"])
    plt.xlabel("Successive Bets")
    plt.ylabel("Winnings ($)")
    plt.title("Roulette Simulation - Median Winnings")
    plt.show()
    plt.savefig("Figure_3") 



    # Figure 4.
    num_episodes = 1000
    num_successive_bets = 1000
    winnings = experiment_2(
        num_episodes
        ,num_successive_bets
        ,win_prob
        )

    mean_winnings = np.zeros(
        (
            num_successive_bets + 1
            ,1
            )
            )
    std_winnings = np.zeros(
        (
            num_successive_bets + 1
            ,1
            )
        )
    
    for i in range(1, num_successive_bets + 1):
        mean_winnings[i] = np.mean(winnings[i])
        std_winnings[i] = np.std(winnings[i])

    data = np.concatenate(
        (
            mean_winnings + std_winnings
            ,mean_winnings
            ,mean_winnings -std_winnings
            )
            ,axis=1
            )

    plt.figure(4)
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.plot(data)
    plt.legend(["Upper", "Mean", "Lower"])
    plt.xlabel("Successive Bets")
    plt.ylabel("Winnings ($)")
    plt.title("Roulette Simulation - Mean Winnings")
    plt.show()
    plt.savefig("Figure_4") 



    # Figure 5.
    num_episodes = 1000
    num_successive_bets = 1000
    winnings = experiment_2(
        num_episodes
        ,num_successive_bets
        ,win_prob
        )

    median_winnings = np.zeros(
        (
            num_successive_bets + 1
            ,1
            )
            )
    std_winnings = np.zeros(
        (
            num_successive_bets + 1
            ,1
            )
        )
    
    for i in range(1, num_successive_bets + 1):
        median_winnings[i] = np.median(winnings[i])
        std_winnings[i] = np.std(winnings[i])

    data = np.concatenate(
        (
            median_winnings + std_winnings
            ,median_winnings
            ,median_winnings -std_winnings
            )
            ,axis=1
            )

    plt.figure(5)
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.plot(data)
    plt.legend(["Upper", "Median", "Lower"])
    plt.xlabel("Successive Bets")
    plt.ylabel("Winnings ($)")
    plt.title("Roulette Simulation - Median Winnings")
    plt.show()
    plt.savefig("Figure_5") 


if __name__ == "__main__":  		  	   		 	 	 			  		 			     			  	 
    test_code()  		  	   		 	 	 			  		 			     			  	 

