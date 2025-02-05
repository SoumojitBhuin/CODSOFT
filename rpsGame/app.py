from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Global dictionary to store round data and scores
game_data = {
    "rounds": []  # To store all round results
}
final_score={"user":0,"computer":0} # Current scores


# Choices for the game
choices = ["Rock", "Paper", "Scissors"]

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "User"
    else:
        return "Computer"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_choice = request.form["choice"]
        computer_choice = random.choice(choices)
        winner = determine_winner(user_choice, computer_choice)

        # Update scores
        if winner == "User":
            final_score["user"] += 1
        elif winner == "Computer":
            final_score["computer"] += 1

        # Store the round result
        game_data["rounds"].append({
            "user_choice": user_choice,
            "computer_choice": computer_choice,
            "winner": winner
        })

        return redirect(url_for("home"))

    return render_template("index.html", rounds=game_data["rounds"], scores=final_score)

@app.route("/reset")
def reset():
    # Reset the game data
    game_data["rounds"] = []
    final_score["user"] = final_score["computer"] = 0
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
