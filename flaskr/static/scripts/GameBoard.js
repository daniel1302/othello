class GameBoard
{
	static get WHITE() { return '#ffffff'; }
	static get BLACK() { return '#000000'; }
	static get EVENT_CLICK() { return 'click'; }
	static get PAWN_WHITE() { return 1; }
	static get PAWN_BLACK() { return 2; }


	constructor(canvas, cols, rows) {
		this.canvas = canvas;
		this.ctx = canvas.getContext('2d');
		this.cols = cols;
		this.rows = rows;

		// Board settings
		this.tileSize = 40;
		this.bgColor = '#80AE70';
		this.lineWidth = 0.3;
		this.borderWidth = 2;
		this.borderColor = '#4E6649';
		this.lineColor = '#4E6649';

		this._resizeCanvas()
	}

	get width() {
		return this.cols * this.tileSize;
	}

	get height() {
		return this.rows * this.tileSize;
	}

	get fullWidth() {
		return 2 * this.borderWidth
				+ (this.cols - 1) * this.lineWidth
				+ this.width;
	}

	get fullHeight() {
		return 2 * this.borderWidth
				+ (this.rows - 1) * this.lineWidth
				+ this.height;
	}

	_resizeCanvas() {
		this.canvas.width = this.fullWidth;
		this.canvas.height = this.fullHeight;
	}

	_drawBackground() {
		this.ctx.fillStyle = this.bgColor;
		this.ctx.clearRect(0, 0, this.fullWidth, this.fullHeight)
		this.ctx.fillRect(0, 0, this.fullWidth, this.fullHeight);
	}

	_tilePos(col, row) {
		if (col > this.cols || row > this.rows) {
			throw 'Out of game board range';
		}

		return [
			this.borderWidth + col*this.tileSize + col*this.lineWidth,
			this.borderWidth + row*this.tileSize + row*this.lineWidth,
		];
	}

	_drawLines() {
		let pos;
		this.ctx.strokeStyle = this.lineColor;
		this.ctx.lineWidth = this.lineWidth;

		for (let col=1; col<this.cols; col++) {
			pos = this._tilePos(col, 0);
			this.ctx.moveTo(pos[0], 0);
			this.ctx.lineTo(pos[0], this.fullHeight);
		}
		for (let row=1; row<this.cols; row++) {
			pos = this._tilePos(0, row);
			this.ctx.moveTo(0, pos[1]);
			this.ctx.lineTo(this.fullWidth, pos[1]);
		}

		this.ctx.stroke();
	}

	_drawBorder() {
		this.ctx.strokeStyle = this.borderColor;
		this.ctx.lineWidth = this.borderWidth;
		this.ctx.strokeRect(0, 0, this.fullWidth, this.fullHeight);
	}

	_drawPawns(boardState) {
		console.log(boardState.length);
		if (boardState.length != this.cols) {
			throw 'Invalid board size(cols)';
		}

		for (let x=0; x<this.cols; x++) {
			if (boardState[x].length != this.rows) {
				throw 'Invalid board size(rows)';
			}

			for (let y=0;y<this.rows; y++) {
				if (boardState[x][y] == GameBoard.PAWN_WHITE) {
					this.drawPawn(x, y, GameBoard.WHITE);
				} else if (boardState[x][y] == GameBoard.PAWN_BLACK) {
					this.drawPawn(x, y)
				}
			}
		}
	}

	redraw(boardState) {
		this._drawBackground();
		this._drawBorder();
		this._drawLines();
		this._drawPawns(boardState)
	}

	drawPawn(col, row, color=GameBoard.BLACK) {
		console.log(col, row, color);
		let pos = this._tilePos(col, row);
		pos[0] += this.tileSize/2;
		pos[1] += this.tileSize/2;


		this.ctx.beginPath();
		this.ctx.arc(pos[0], pos[1], (this.tileSize*0.8)/2, 0, 2 * Math.PI);
		this.ctx.closePath();
		this.ctx.stroke();
		this.ctx.fillStyle = color;
		this.ctx.fill();
	}

	registerEvent(type, callback) {
		let allowedEvents = [GameBoard.EVENT_CLICK];

		if (!allowedEvents.includes(type)) {
			return;
		}

		let canvas = this.canvas;
		let borderWidth = this.borderWidth;
		let lineWidth = this.lineWidth;
		let tileSize = this.tileSize;
		let that = this;
		this.canvas.addEventListener(type, function (evt) {
			let rect = canvas.getBoundingClientRect();

			let clicked = {
				x: evt.clientX - rect.left - borderWidth,
				y: evt.clientY - rect.top - borderWidth
			};

			clicked.x = parseInt(clicked.x / (tileSize + lineWidth));
			clicked.y = parseInt(clicked.y / (tileSize + lineWidth));

			that._tilePos(clicked.x, clicked.y);

			callback(clicked);
		});
	}
}