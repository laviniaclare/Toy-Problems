"""
Write an interactive guessing game. The program should pick a number from 1 - 100,
ask the user for a guess, and then let them know if their guess is too high, too low, or correct.
When the user guesses correctly, exit the program
"""

def guessing_game
    number = rand(1..100)

    puts "hello, please guess a number between 1 and 100"
    while true
        guess = STDIN.gets().to_i
        puts "you guessed: #{guess}"
        
        if guess > number
            puts "that's too high, try again!"
        elsif guess < number
            puts "that's too low, try again!"
        else
            puts "You win!!"
            puts "Thank you for playing"
            break
        end
    end
end


guessing_game()