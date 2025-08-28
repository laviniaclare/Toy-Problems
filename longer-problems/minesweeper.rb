# Minesweeper game. Should print the grid as a string. should have a method to auto-play a game.
# if a mine is hit, the game should end and print the grid with the mines.
# if a square is selected, it should reveal all adjacent squares that are not mines.
# if a square is flagged, it should be marked as such.
# if a square is unflagged, it should be marked as such.
# if a square is revealed, it should be marked as such.
# if a square is unrevealed, it should be marked as such.
# if a square is selected and there are no adjacent mines, it should reveal all adjacent squares that are not mines.
# if a square is selected and there are adjacent mines, it should reveal only that square and mark the number of adjacent mines.

class Board
  attr_accessor :rows, :cols, :mines
  def initialize(rows, cols, mines)
    @rows = rows
    @cols = cols
    @mines = mines
    @board = generate_board()
    @mine_locations = place_mines()
    @game_over = false
  end

  def print_board
    @board.each do |row|
      puts row.join(" ")
    end
  end

  def game_over?
    @game_over
  end

  def make_move(x, y)
    if @mine_locations.include?([x,y])
      @board[x][y] = "X"
      @game_over = true
      reveal_board()
    else
      @board[x][y] = "|"
      reveal_adjacent_squares(x,y)
    end
  end

  private
  def generate_board
    board = []
    @rows.times do
      row = []
      @cols.times do
        row.append("-")
      end
      board.append(row)
    end
    board
  end

  def place_mines
    mine_locations = []
    @mines.times do
      x = rand(0...@rows)
      y = rand(0...@cols)
      mine_locations.append([x,y])
    end
    mine_locations
  end

  def reveal_adjacent_squares(x,y)
    # get adjacent square coordinates
    # for each adjacent square
    # if it is a mine, do nothing
    # if it's not a mine, count the adjacent mines and change value to count
  end

  def get_adjacent_square_coords(x,y)
  end

  def count_adjacent_mines(x,y)
  end

  def reveal_board
    # print board with all mines shown
  end
end

class Minesweeper
  def initialize
    @rows = 10
    @cols = 10
    @mines = 10
  end

  def play
    pp "Let's play!"
    board = Board.new(10, 10, 10)
    board.print_board

    while true
      x = rand(0...@rows)
      y = rand(0...@cols)

      board.make_move(x, y)
      if board.game_over?
        puts "Game over!"
        board.print_board
        break
      else
        pp "  "
        pp "Pick your next move"
        pp "**************************"
        board.print_board
      end
    end
  end  
end

Minesweeper.new.play
 
