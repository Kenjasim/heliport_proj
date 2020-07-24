class Heliport():
    """
    Class which represents a heliport
    """

    def __init__(self, spaces):
        """
        Initialises all the variables about the heliport
        """
        self.spaces = spaces
        self.filled_spaces = 0
        self.helicopters = []

    def get_spaces(self):
        """
        Returns the amount of spaces left
        """
        return self.spaces - self.filled_spaces

    def get_helicopters(self):
        """
        Returns the helicopters in the helipad
        """
        return self.helicopters

    def add_helicopter(self, string):
        """
        Adds the helocopter to the helipad unless
        it is full
        """
        if (self.filled_spaces == self.spaces):
            return 1
        else:
            self.helicopters.append(string)
            self.filled_spaces += 1
            return 0

    def delete_helicopter(self, string):
        """
        Removes the helocopter from the helipad unless
        it is empty
        """
        if (self.filled_spaces == 0):
            return 1
        else:
            self.helicopters.remove(string)
            self.filled_spaces -= 1

    
class Helicopter():
    """
    Class which represents a helicopter
    """

    def __init__(self, name):
        """
        Initialises all the variables about the helicopter
        """
        self.name = name
        self.status = "flying"
        self.heliport = None

    def land(self, heliport):
        """
        Lands at a heliport
        """
        if self.status is "landed":
            return 2
        else:
            h = heliport.add_helicopter(self.name +":" + str(id(self)))
            if h == 1:
                return h
            else:
                self.heliport = heliport
                self.status = "landed"
                return 0

    def take_off(self):
        """
        Comences takeoff
        """
        if self.status is "flying":
            return 2
        else:
            h = self.heliport.delete_helicopter(self.name +":" + str(id(self)))
            if h == 1:
                return h
            else:
                self.status = "flying"
                self.heliport = None
                return 0

    def get_name(self):
        return self.name

    def get_id(self):
        return id(self)

    def get_heliport(self):
        return self.heliport

    def get_status(self):
        return self.status
