import asyncio

class GameState:
    def __init__(self, guild, channel):
        self.guild = guild
        self.channel = channel

        self.phase = "waiting"
        self.players = []
        self.roles = {}
        self.alive = set()

        self.day_count = 0
        self.loop_task = None

        self.night_time = 20
        self.day_time = 40
        self.vote_time = 20

    # =========================
    # ゲーム開始
    # =========================
    async def start(self):
        self.alive = {p.id for p in self.players}
        self.loop_task = asyncio.create_task(self.game_loop())

    # =========================
    # メインループ（最重要）
    # =========================
    async def game_loop(self):
        while True:

            # 🌙 夜
            self.phase = "night"
            await self.channel.send("🌙 夜になりました")
            await asyncio.sleep(self.night_time)

            # （今は処理なし）

            # 勝利判定（仮）
            if self.check_win():
                break

            # ☀ 昼
            self.phase = "day"
            self.day_count += 1
            await self.channel.send(f"☀ 昼になりました（{self.day_count}日目）")
            await asyncio.sleep(self.day_time)

            # 🗳 投票
            self.phase = "vote"
            await self.channel.send("🗳 投票時間です")
            await asyncio.sleep(self.vote_time)

            # 勝利判定（仮）
            if self.check_win():
                break

    # =========================
    # 仮勝利判定
    # =========================
    def check_win(self):
        return False
