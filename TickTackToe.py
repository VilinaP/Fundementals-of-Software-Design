#Tick Tak Toe
#Vilina Prenko
#14.11.2025 - create the class and start drawing(figure out how to draw in PySide6).
#16.11.2025 - continue drawing (I have no clue what is happening)
#17.11.2025 - drawing elements, and more drawing, finish drawing, score board
#18.11.2025 - check for the winner, add restart, track whose turn, implement the x,t tracking for PySide6
#19.11.2025 - put everything together and finish the project, test all of the parts manually, design
#11.12.2025 - creating the scalable board


'''To change the size of the board go to the comment in the MainWindow(), where TickTackToe in called, Line 230'''

from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QVBoxLayout,
    QPushButton, 
    QLabel, 
    QHBoxLayout,
    QDialog,
    QDialogButtonBox,
)
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt, QRectF, QPointF, Signal

class TicTacToe(QWidget):
    state_changed = Signal()

    def __init__(self, size):
        super().__init__()

        self.field_size = size
        self.board = [[None]*self.field_size for _ in range(self.field_size)]
        self.current_player = 'X'
        self.winner = None
        self.winning_cells = None

        self.XWins = 0
        self.OWins = 0
        self.draws = 0


    def reset(self):
        self.board = [[None]*self.field_size for _ in range(self.field_size)]
        self.current_player = 'X'
        self.winner = None
        self.winning_cells = None
        self.update()

    def mousePressEvent(self, event):
        if self.winner is not None:
            return
        else:
            pos = event.pos()
        x = pos.x()
        y = pos.y()

        cell_w = self.width() / self.field_size
        cell_h = self.height() / self.field_size

        col = int(x // cell_w)
        row = int(y // cell_h)
        if 0 <= row < self.field_size and 0 <= col < self.field_size:
            if self.board[row][col] is None:
                self.board[row][col] = self.current_player
                self.winner, self.winning_cells = self.check_winner()

                if self.winner == 'X':
                    self.XWins += 1
                elif self.winner == 'O':
                    self.OWins += 1

                if self.winner is None:
                    if all(all(c is not None for c in row_) for row_ in self.board):
                        self.winner = 'Draw'
                        self.draws += 1
                    else:
                        self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.update()
                self.state_changed.emit()

    def check_winner(self):
        '''
        >>> game = TicTacToe(3)
        >>> game.board = [
        ...     ['X','X','X'],
        ...     [None,'O','O'],
        ...     [None,None,None]
        ... ]
        >>> game.check_winner()
        ('X', [(0, 0), (0, 1), (0, 2)])

        >>> game = TicTacToe(3)
        >>> game.board = [
        ...     ['X','O',None],
        ...     ['O','X',None],
        ...     ['O',None,'X']
        ... ]
        >>> game.check_winner()
        ('X', [(0, 0), (1, 1), (2, 2)])

        ''' 


        # rows
        for r in range(self.field_size):
            if self.board[r][0] and all(self.board[r][c] == self.board[r][0] for c in range(self.field_size)):
                return self.board[r][0], [(r, c) for c in range(self.field_size)]

        # columns
        for c in range(self.field_size):
            if self.board[0][c] and all(self.board[r][c] == self.board[0][c] for r in range(self.field_size)):
                return self.board[0][c], [(r, c) for r in range(self.field_size)]

        # main diagonal
        if self.board[0][0] and all(self.board[i][i] == self.board[0][0] for i in range(self.field_size)):
            return self.board[0][0], [(i, i) for i in range(self.field_size)]

        # anti diagonal
        # all() перевіряє чи є там якась фігня
        if self.board[0][self.field_size-1] and all(self.board[i][self.field_size-1-i] == self.board[0][self.field_size-1] for i in range(self.field_size)):
            return self.board[0][self.field_size-1], [(i, self.field_size-1-i) for i in range(self.field_size)]
        
        return None, None

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        w = self.width()
        h = self.height()
        cell_w = w / self.field_size
        cell_h = h / self.field_size
        size_unit = min(cell_w, cell_h)

        # Міняєм колір фону
        painter.fillRect(0, 0, w, h, QColor(255, 182, 193))
        # Колір ліній
        pen = QPen(QColor(231, 84, 128))

        pen.setWidth(max(2, int(size_unit * 0.06)))
        painter.setPen(pen)
        
        for i in range(1, self.field_size):
            x = i * cell_w
            painter.drawLine(int(x), 0, int(x), h)
        for i in range(1, self.field_size):
            y = i * cell_h
            painter.drawLine(0, int(y), w, int(y))

        # Малюю Х та О
        mark_pen = QPen() #change the color for X and O
        mark_pen.setCapStyle(Qt.RoundCap)
        mark_pen.setJoinStyle(Qt.RoundJoin)
        mark_pen.setWidth(max(2, int(size_unit * 0.12)))

        for r in range(self.field_size):
            for c in range(self.field_size):
                mark = self.board[r][c]
                left = c * cell_w
                top = r * cell_h
                rect = QRectF(left, top, cell_w, cell_h)

                if mark == 'X':
                    painter.setPen(mark_pen)
                    margin = size_unit * 0.18
                    p1 = QPointF(rect.left() + margin, rect.top() + margin)
                    p2 = QPointF(rect.right() - margin, rect.bottom() - margin)
                    p3 = QPointF(rect.left() + margin, rect.bottom() - margin)
                    p4 = QPointF(rect.right() - margin, rect.top() + margin)
                    painter.drawLine(p1, p2)
                    painter.drawLine(p3, p4)
                elif mark == 'O':
                    painter.setPen(mark_pen)
                    margin = size_unit * 0.18
                    orect = QRectF(rect.left() + margin, rect.top() + margin,
                                   rect.width() - 2*margin, rect.height() - 2*margin)
                    painter.drawEllipse(orect)

        # Highlight winning line
        if self.winner and self.winner != 'Draw' and self.winning_cells:
            highlight_pen = QPen(QColor(200, 30, 30, 220))
            highlight_pen.setWidth(max(3, int(size_unit * 0.14)))
            highlight_pen.setCapStyle(Qt.RoundCap)
            painter.setPen(highlight_pen)

            cells = self.winning_cells
            def center_of(cell):
                rr, cc = cell
                cx = (cc + 0.5) * cell_w
                cy = (rr + 0.5) * cell_h
                return QPointF(cx, cy)
            start = center_of(cells[0])
            end = center_of(cells[-1])
            painter.drawLine(start, end)

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(255, 182, 193); color: black;")
        self.setWindowTitle('Restart')

        QBtn = (
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel(f"Are you sure you want to restart the game?")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(8,8,8,8)
        layout.setSpacing(6)

        self.setMinimumSize(600, 500)

        #Call for Tick Tack Toe (can edit the number of squares)
        self.game = TicTacToe(3)

        layout.addWidget(self.game, stretch=1)
        score_container = QWidget()
        score_layout = QVBoxLayout(score_container)

        self.x_label = QLabel("X Wins: 0")
        self.o_label = QLabel("O Wins: 0")
        self.draw_label = QLabel("Draws: 0")

        for lbl in (self.x_label, self.o_label, self.draw_label):
            lbl.setStyleSheet("color: white; font-size: 18px;")

        #Можна використовувати CSS 
        score_layout.addWidget(QLabel(
            "<b><p style='color:white; font-size:20px;'>Scoreboard</p></b>"
        ))
        score_layout.addWidget(self.x_label)
        score_layout.addWidget(self.o_label)
        score_layout.addWidget(self.draw_label)
        score_layout.addStretch()

        row_layout = QHBoxLayout()
        row_layout.addWidget(self.game, stretch=3)
        row_layout.addWidget(score_container, stretch=1)

        
        layout.insertLayout(0, row_layout, stretch=1)
        controls = QHBoxLayout()
        self.status_label = QLabel()
        controls.addWidget(self.status_label)
        controls.addStretch(1)
        self.reset_btn = QPushButton("Restart")
        self.reset_btn.clicked.connect(self.on_restart)
        controls.addWidget(self.reset_btn)
        layout.addLayout(controls)

        # update label whenever game state changes
        self.game.state_changed.connect(self.update_status_label)
        self.update_status_label()
        self.resize(480, 540)

    def on_restart(self):
        dialog = Dialog()
        if dialog.exec():
            self.game.reset()
            self.status_label.setText(f"Turn: X")

    def update_status_label(self):
        if self.game.winner is None:
            self.status_label.setText(f"Turn: {self.game.current_player}")
        elif self.game.winner == 'Draw':
            self.status_label.setText("Game over: Draw")
        else:
            self.status_label.setText(f"Game over: Winner — {self.game.winner}")
        self.x_label.setText(f"X Wins: {self.game.XWins}")
        self.o_label.setText(f"O Wins: {self.game.OWins}")
        self.draw_label.setText(f"Draws: {self.game.draws}")

if __name__ == "__main__":
    app = QApplication()
    win = MainWindow()
    import doctest
    doctest.testmod()
    win.show()
    app.exec()
