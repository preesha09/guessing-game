import streamlit as st

st.title("🎮 Tic Tac Toe")

# Initialize board
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None

def check_winner(board):
    win_patterns = [
        (0,1,2), (3,4,5), (6,7,8),   # rows
        (0,3,6), (1,4,7), (2,5,8),   # columns
        (0,4,8), (2,4,6)             # diagonals
    ]
    for a, b, c in win_patterns:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "Tie"
    return None

# Reset the game
if st.button("Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None

# Game grid UI
cols = st.columns(3)
for i in range(9):
    if cols[i % 3].button(st.session_state.board[i] or " ", key=i):
        if st.session_state.board[i] == "" and not st.session_state.winner:
            st.session_state.board[i] = st.session_state.current_player
            st.session_state.winner = check_winner(st.session_state.board)
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# Show game status
if st.session_state.winner == "Tie":
    st.info("It's a tie! 🤝")
elif st.session_state.winner:
    st.success(f"Player {st.session_state.winner} wins! 🎉")
else:
    st.write(f"Current Player: **{st.session_state.current_player}**")
