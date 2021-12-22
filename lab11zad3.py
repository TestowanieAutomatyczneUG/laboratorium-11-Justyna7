# Napisz klasę FriendShips, która będzie zawierała słownik, gdzie kluczem będzie ciąg tekstowy, a wartościami lista z ciągami tekstowymi.
#
# Przykład słownika:
#
# {
#     "Miotk": ["Kowalski", "Nowak", "Bobkowska"]
# }
# Klasa ta ma zawierać następujące metody:
#
# makeFriends(person1, person2) - dodaje person1 oraz person2 jako przyjaciół, korzystając z metody addFriend
# getFriendsList(person) - pobiera listę przyjaciół person
# areFriends(person1, person2) - sprawdzenie czy person1 jest przyjacielem person2
# addFriend(person, friend) - dodanie friend jako przyjaciela person
# Przetestuj powyższe metody za pomocą unittest. Następnie utwórz klasę, która będzie implementować przechowywanie klasy
# FriendShips w systemie bazodanowym. Przetestuj tę klasę przy użyciu MagicMock. Użyj sprawdzenia metod wywołania metod (assert_call_with itd oraz side_effects).
#
# Rozwiązanie umieść w serwisie github pod linkiem: https://classroom.github.com/a/j7lrZ3bL
import unittest


class FriendShips:
    def __init__(self):
        self.slownik = {"Miotk": ["Kowalski", "Nowak", "Bobkowska"]}

    def makeFriends(self, person1, person2):
        self.addFriend(person1, person2)
        self.addFriend(person2, person1)

    def getFriendsList(self, person):
        if person in self.slownik:
            return self.slownik[person]
        else:
            raise Exception

    def areFriends(self, person1, person2):
        if person1 in self.slownik:
            if person2 in self.slownik[person1]:
                return True
            else:
                return False
        return False

    def addFriend(self, person, friend):
        if person in self.slownik:
            if friend not in self.slownik[person]:
                self.slownik[person].append(friend)
        else:
            self.slownik[person] = [friend]


class test_FriendShips(unittest.TestCase):
    def setUp(self):
        self.f = FriendShips()

    def test_are_friends_Miotk_Kowalski(self):
        self.assertEqual(True, self.f.areFriends("Miotk", "Kowalski"))

    def test_are_friends_Kowalski_Miotk(self):
        self.assertEqual(False, self.f.areFriends("Kowalski", "Miotk"))

    def test_make_friends_Kowalski_Miotk(self):
        self.f.makeFriends("Kowalski", "Miotk")
        self.assertEqual(True, self.f.areFriends("Kowalski", "Miotk"))

    def test_make_friends_Nowak_Bobkowska(self):
        self.f.makeFriends("Bobkowska", "Nowak")
        self.assertEqual(True, self.f.areFriends("Bobkowska", "Nowak"))

    def test_get_friend_list(self):
        self.assertEqual(["Kowalski", "Nowak", "Bobkowska"], self.f.getFriendsList("Miotk"))

    def test_make_friends_Kowalski_Kowal(self):
        self.f.makeFriends("Kowalski", "Miotk")
        self.f.makeFriends("Kowalski", "Kowal")
        self.assertEqual(["Miotk", "Kowal"], self.f.getFriendsList("Kowalski"))

    def test_get_friends_list_Exceptions(self):
        self.assertRaises(Exception, self.f.getFriendsList, "Bobkowska")

    def tearDown(self):
        self.f = None

if __name__ == '__main__':
    unittest.main()