var newGame = document.getElementById("newGame");
var toggleRecords = document.getElementById("toggleRecords");
var board = document.getElementById("board");
var records = document.getElementById("records");
var recordsList = document.getElementById("recordsList");

var grid = [];
var currentPlayer = 'white';
var selectedRow = null;
var selectedCol = null;
var gameActive = true;
var currentScore = 0;

function initGrid() {
    grid = []
    for (let r = 0; r < 8; r++) {
        grid[r] = [];
        for (let c = 0; c < 8; c++) {
            grid[r][c] = null;
        }
    }
    for (let r = 0; r < 8; r++) {
        for (let c = 0; c < 8; c++) {
            if ((r + c) % 2 === 1) {
                if (r < 3) {
                    grid[r][c] = 'black';
                }
                else if (r > 4) {
                    grid[r][c] = 'white';
                }
            }
        }
    }
}
function renderBoard() {
    board.innerHTML = '';
    board.style.display = 'grid';
    for (let r = 0; r < 8; r++) {
        for (let c = 0; c < 8; c++) {
            let cell = document.createElement('div');
            cell.style.width = '50px';
            cell.style.height = '50px';
            cell.style.display = 'flex';
            cell.style.alignItems = 'center';
            cell.style.justifyContent = 'center';
            cell.style.fontSize = '32px';
            if ((r + c) % 2 === 1) {
                cell.style.backgroundColor = '#403d3dff';
            } else {
                cell.style.backgroundColor = '#e0d7c7ff';
            }
            if (grid[r][c] === 'black') {
                let piece = document.createElement('div');
                piece.style.width = '40px';
                piece.style.height = '40px';
                piece.style.borderRadius = '50%';
                piece.style.backgroundColor = '#000';
                cell.appendChild(piece);
            } else if (grid[r][c] === 'white') {
                let piece = document.createElement('div');
                piece.style.width = '40px';
                piece.style.height = '40px';
                piece.style.borderRadius = '50%';
                piece.style.backgroundColor = '#fff';
                cell.appendChild(piece);
            }
            board.appendChild(cell);
        }
    }
}
initGrid();
renderBoard();
console.log(grid);
