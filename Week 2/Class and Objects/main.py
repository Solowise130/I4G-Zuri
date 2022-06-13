class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self):
        self.score = None
        self.track = None
        self.age = None
        self.name = None

    def _init_(self,name, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.scores = float(score)
    def change_name(self,new_name):
        self.name = new_name
        "new_name = Peter"
        print(f"the student updated his name to (new_name)")

    def change_age (self, new_age):
        self.age = new_age
        "new_age = 34"
        print(f"the student updated his age to (new_age) years old")

    def add_track (self, new_tracks):
        self.track = new_tracks
        "new_tracks = UX/UX"
        print(f"the student updated his track record to (new_track)")

    def get_score (self,new_score):
        self.score = new_score
        "new_score = 3.1"
        print(f"the student updated his score to (new_score)")


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
