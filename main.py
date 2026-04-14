import tkinter as tk
from tkinter import messagebox


PLAYER_X = "X"
PLAYER_O = "O"

COLORS = {
    "bg": "#1e1e2e",
    "cell_bg": "#313244",
    "cell_hover": "#45475a",
    "X": "#f38ba8",
    "O": "#89b4fa",
    "status_text": "#cdd6f4",
    "grid": "#6c7086",
}


class TicTacToe:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)
        self.root.configure(bg=COLORS["bg"])

        self.current_player = PLAYER_X
        self.board: list[str | None] = [None] * 9
        self.buttons: list[tk.Button] = []
        self.game_over = False

        self._build_ui()

    # ------------------------------------------------------------------ #
    # UI construction
    # ------------------------------------------------------------------ #

    def _build_ui(self) -> None:
        self._build_status_bar()
        self._build_grid()
        self._build_restart_button()

    def _build_status_bar(self) -> None:
        self.status_var = tk.StringVar(value=f"Player {PLAYER_X}'s turn")
        status = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=("Helvetica", 16, "bold"),
            bg=COLORS["bg"],
            fg=COLORS["status_text"],
            pady=12,
        )
        status.pack()

    def _build_grid(self) -> None:
        grid_frame = tk.Frame(self.root, bg=COLORS["grid"], padx=3, pady=3)
        grid_frame.pack(padx=20)

        for i in range(9):
            row, col = divmod(i, 3)
            btn = tk.Button(
                grid_frame,
                text="",
                font=("Helvetica", 42, "bold"),
                width=3,
                height=1,
                bg=COLORS["cell_bg"],
                fg=COLORS["status_text"],
                activebackground=COLORS["cell_hover"],
                relief="flat",
                cursor="hand2",
                command=lambda idx=i: self._on_cell_click(idx),
            )
            btn.grid(row=row, column=col, padx=2, pady=2)
            btn.bind("<Enter>", lambda e, b=btn: self._on_hover(b, True))
            btn.bind("<Leave>", lambda e, b=btn: self._on_hover(b, False))
            self.buttons.append(btn)

    def _build_restart_button(self) -> None:
        restart = tk.Button(
            self.root,
            text="Restart",
            font=("Helvetica", 13),
            bg=COLORS["cell_bg"],
            fg=COLORS["status_text"],
            activebackground=COLORS["cell_hover"],
            relief="flat",
            cursor="hand2",
            padx=16,
            pady=6,
            command=self._restart,
        )
        restart.pack(pady=14)

    # ------------------------------------------------------------------ #
    # Event handlers
    # ------------------------------------------------------------------ #

    def _on_hover(self, btn: tk.Button, entering: bool) -> None:
        if btn["text"] == "" and not self.game_over:
            btn.configure(bg=COLORS["cell_hover"] if entering else COLORS["cell_bg"])

    def _on_cell_click(self, idx: int) -> None:
        if self.game_over or self.board[idx]:
            return

        self.board[idx] = self.current_player
        color = COLORS[self.current_player]
        self.buttons[idx].configure(text=self.current_player, fg=color, bg=COLORS["cell_bg"])

        if self._check_winner():
            self._highlight_winner()
            self.status_var.set(f"Player {self.current_player} wins!")
            self.game_over = True
            return

        if all(self.board):
            self.status_var.set("It's a draw!")
            self.game_over = True
            return

        self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X
        self.status_var.set(f"Player {self.current_player}'s turn")

    # ------------------------------------------------------------------ #
    # Game logic
    # ------------------------------------------------------------------ #

    WIN_LINES = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6),              # diagonals
    ]

    def _check_winner(self) -> tuple[int, int, int] | None:
        for line in self.WIN_LINES:
            a, b, c = line
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                return line
        return None

    def _highlight_winner(self) -> None:
        line = self._check_winner()
        if line:
            color = COLORS[self.current_player]
            for idx in line:
                self.buttons[idx].configure(bg=color, fg=COLORS["bg"])

    def _restart(self) -> None:
        self.board = [None] * 9
        self.current_player = PLAYER_X
        self.game_over = False
        self.status_var.set(f"Player {PLAYER_X}'s turn")
        for btn in self.buttons:
            btn.configure(text="", bg=COLORS["cell_bg"], fg=COLORS["status_text"])


def main() -> None:
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()


if __name__ == "__main__":
    main()
