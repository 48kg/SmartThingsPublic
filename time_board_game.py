import random

class Age:
    def __init__(self, name, tech_queue):
        self.name = name
        self.tech_queue = list(tech_queue)
        self.techs = []
        self.population = 100
        self.efficiency = 1.0

    def progress(self):
        if self.tech_queue:
            self.techs.append(self.tech_queue.pop(0))
        # population grows with efficiency
        self.population = int(self.population * (1 + 0.05 * self.efficiency))

    def __str__(self):
        return f"{self.name}: pop={self.population}, eff={self.efficiency:.2f}, techs={self.techs}"

class Game:
    def __init__(self):
        self.ages = [
            Age('Stone Age', ['Fire', 'Wheel']),
            Age('Middle Ages', ['Castle', 'Alchemy']),
            Age('Modern Age', ['Internet', 'Nuclear Power']),
            Age('Future', ['Quantum AI', 'Fusion'])
        ]
        self.year = 1
        self.loop_interval = 10
        self.max_year = 100
        self.events = [
            self.event_time_storm,
            self.event_future_virus,
            self.event_war
        ]

    def event_time_storm(self):
        age = random.choice(self.ages)
        age.efficiency *= 0.5
        print(f"Tidsstorm i {age.name}! Effektivitet halveret.")

    def event_future_virus(self):
        age = self.ages[2]  # Modern Age
        age.population = int(age.population * 0.7)
        print("Fremtidsvirus lækker til 2025! Befolkningen falder drastisk.")

    def event_war(self):
        age = random.choice(self.ages[:2])
        age.population = int(age.population * 0.8)
        print(f"Krige raser i {age.name}! Befolkningen lider tab.")

    def random_event(self):
        if random.random() < 0.3:  # 30% chance each year
            random.choice(self.events)()

    def loop_menu(self):
        print("\n-- Tidsloop! Du kan overføre en teknologi --")
        for idx, age in enumerate(self.ages):
            print(f"{idx}: {age.name} -> {age.techs}")
        try:
            src = int(input("Vælg kilde-alder: "))
            dst = int(input("Vælg mål-alder: "))
            if src == dst or src not in range(4) or dst not in range(4):
                print("Ugyldigt valg.")
                return
            if not self.ages[src].techs:
                print("Ingen teknologier at overføre.")
                return
            tech = self.ages[src].techs.pop()
            self.ages[dst].techs.append(tech)
            print(f"Overførte {tech} fra {self.ages[src].name} til {self.ages[dst].name}.")
        except Exception as e:
            print("Fejl i tidsloop.", e)

    def play_turn(self):
        print(f"\n===== År {self.year} =====")
        for age in self.ages:
            age.progress()
        self.random_event()
        for age in self.ages:
            print(age)
        if self.year % self.loop_interval == 0:
            self.loop_menu()
        self.year += 1

    def score(self):
        return sum(age.population + 10 * len(age.techs) for age in self.ages)

    def play(self):
        while self.year <= self.max_year:
            self.play_turn()
        print("\nSpillet er slut!")
        print(f"Slutscore: {self.score()}")
        for age in self.ages:
            print(age)

if __name__ == '__main__':
    Game().play()
