import sys
import math

from PySide6.QtWidgets import (QApplication, QComboBox, QMessageBox, QMainWindow,
                               QGridLayout, QGroupBox, QLabel, QLineEdit,
                               QPushButton, QVBoxLayout, QWidget)
from PySide6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.flag_wrong_input = [0, 0, 0, 0, 0, 0, 0, 0]
        self.flag_blank_input = [1, 1, 1, 1, 1, 1, 1, 1]
        self.flag_range_input = [0, 0, 0, 0]

        self.resistance = 0
        self.inductance = 0
        self.capacitance = 0
        self.line_capacity = 0

        #default values for narrow base tower
        self.current_tower_type = 0

        #default number of circuits
        self.current_number_of_circuits = 1

        #default coordinates 
        self.current_x1_line = 0
        self.current_y1_line = 0
        self.current_x2_line = 0
        self.current_y2_line = 0
        self.current_x3_line = 0
        self.current_y3_line = 0

        #default number of conductors
        self.current_number_of_conductors = 1

        #default distance between the conductors
        self.current_distance_between_conductors = 0

        #defualt values for hawk conductor
        self.current_conductor_type = 0
        self.diameter = 21.793
        self.conductor_gmr = 8.809
        self.ac_resistance = 0.132
        self.current_capacity = 659

        #default length of tl
        self.current_length_of_tl = 0

        self.create_tower_type_box()
        self.create_number_of_circuits_box()
        self.create_coordinates_box()
        self.create_number_of_conductors_box()
        self.create_distance_between_conductors_box()
        self.create_conductor_type_box()
        self.create_length_of_tl_box()
        self.create_tower_information_box()

        calculate = QPushButton("Calculate")
        calculate.clicked.connect(self.calculate_clicked)

        main_layout = QGridLayout()
        main_layout.addWidget(self._tower_type_box, 0, 0)
        main_layout.addWidget(self._number_of_circuits_box, 1, 0)
        main_layout.addWidget(self._coordinates_box, 2, 0)
        main_layout.addWidget(self._number_of_conductors_box, 3, 0)
        main_layout.addWidget(self._distance_between_conductors_box, 4, 0)
        main_layout.addWidget(self._conductor_type_box, 5, 0)
        main_layout.addWidget(self._length_of_tl_box, 6, 0)
        main_layout.addWidget(self._tower_information_box, 0, 1, 7, 1)
        main_layout.addWidget(calculate, 7, 0, 1, 2)
 
        self.setWindowTitle("EE374 Project Group 33")

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def create_tower_type_box(self):
        self._tower_type_box = QGroupBox("Tower Type")

        self.tower_type = QComboBox()
        self.tower_type.addItems(["Narrow Base Tower", "Delta Tower", "Vertical Tower"])
        self.tower_type.currentIndexChanged.connect(self.tower_type_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.tower_type)

        self._tower_type_box.setLayout(layout)
        
    def create_number_of_circuits_box(self):
        self._number_of_circuits_box = QGroupBox("Number of Circuits")

        self.number_of_circuits = QComboBox()
        self.number_of_circuits.addItem("1")
        self.number_of_circuits.currentIndexChanged.connect(self.number_of_circuits_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.number_of_circuits)

        self._number_of_circuits_box.setLayout(layout)

    def create_coordinates_box(self):
        self._coordinates_box = QGroupBox("X-Y Coordinates of the Phase Lines (m)")

        self.phase1 = QLabel("Phase 1")
        self.x1 = QLabel("X:")
        self.x1_line = QLineEdit()
        self.x1_line.textChanged.connect(self.x1_line_changed)
        self.y1 = QLabel("Y:")
        self.y1_line = QLineEdit()
        self.y1_line.textChanged.connect(self.y1_line_changed)

        self.phase2 = QLabel("Phase 2")
        self.x2 = QLabel("X:")
        self.x2_line = QLineEdit()
        self.x2_line.textChanged.connect(self.x2_line_changed)
        self.y2 = QLabel("Y:")
        self.y2_line = QLineEdit()
        self.y2_line.textChanged.connect(self.y2_line_changed)

        self.phase3 = QLabel("Phase 3")
        self.x3 = QLabel("X:")
        self.x3_line = QLineEdit()
        self.x3_line.textChanged.connect(self.x3_line_changed)
        self.y3 = QLabel("Y:")
        self.y3_line = QLineEdit()
        self.y3_line.textChanged.connect(self.y3_line_changed)

        layout = QGridLayout()
        layout.addWidget(self.phase1, 0,1)
        layout.addWidget(self.x1, 1,0)
        layout.addWidget(self.x1_line, 1,1)
        layout.addWidget(self.y1, 1,2)
        layout.addWidget(self.y1_line, 1,3)

        layout.addWidget(self.phase2, 2,1)
        layout.addWidget(self.x2, 3,0)
        layout.addWidget(self.x2_line, 3,1)
        layout.addWidget(self.y2, 3,2)
        layout.addWidget(self.y2_line, 3,3)

        layout.addWidget(self.phase3, 4,1)
        layout.addWidget(self.x3, 5,0)
        layout.addWidget(self.x3_line, 5,1)
        layout.addWidget(self.y3, 5,2)
        layout.addWidget(self.y3_line, 5,3)

        self._coordinates_box.setLayout(layout)

    def create_number_of_conductors_box(self):
        self._number_of_conductors_box = QGroupBox("Number of Conductors in the Bundle")

        self.number_of_conductors = QComboBox()
        self.number_of_conductors.addItems(["1","2","3"])
        self.number_of_conductors.currentIndexChanged.connect(self.number_of_conductors_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.number_of_conductors)

        self._number_of_conductors_box.setLayout(layout)

    def create_distance_between_conductors_box(self):
        self._distance_between_conductors_box = QGroupBox("The Distance Between the Conductors Inside the Bundle (mm)")

        self.distance_between_conductors = QLineEdit()
        self.distance_between_conductors.textChanged.connect(self.distance_between_conductors_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.distance_between_conductors)

        self._distance_between_conductors_box.setLayout(layout)

    def create_conductor_type_box(self):
        self._conductor_type_box = QGroupBox("Conductor Type")

        self.conductor_type = QComboBox()
        self.conductor_type.addItems(["Hawk", "Drake", "Cardinal", "Rail", "Pheasant"])
        self.conductor_type.currentIndexChanged.connect(self.conductor_type_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.conductor_type)

        self._conductor_type_box.setLayout(layout)

    def create_length_of_tl_box(self):
        self._length_of_tl_box = QGroupBox("Length of the Transmission Line (km)")

        self.length_of_tl = QLineEdit()
        self.length_of_tl.textChanged.connect(self.length_of_tl_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.length_of_tl)

        self._length_of_tl_box.setLayout(layout)

    def create_tower_information_box(self):
        self._tower_information_box = QGroupBox("Tower Information")

        self.tower_image = QLabel()
        self.tower_image.setPixmap(QPixmap('narrow_base_tower.png'))

        layout = QVBoxLayout()
        layout.addWidget(self.tower_image)

        self._tower_information_box.setLayout(layout)
    
    def calculate_clicked(self):
        if self.current_tower_type == 0:
            self.max_ph_line_height = 39
            self.min_ph_line_height = 23
            self.max_hor_distance = 4
            self.min_hor_distance = 2.2
            self.voltage_level = 66000
            self.max_num_conductors = 3

            self.flag_range_input[0] = self.check_elements_in_range([self.current_y1_line, self.current_y2_line, self.current_y3_line], self.min_ph_line_height, self.max_ph_line_height)
            self.flag_range_input[1] = self.check_elements_in_range([self.current_x2_line, self.current_x3_line], self.min_hor_distance, self.max_hor_distance)
            self.flag_range_input[2] = self.check_elements_in_range([self.current_x1_line], -self.max_hor_distance, -self.min_hor_distance)

        elif self.current_tower_type == 1:
            self.max_ph_line_height = 43
            self.min_ph_line_height = 38.25
            self.max_hor_distance = 11.5
            self.min_hor_distance = 9.4
            self.max_hor_distance_center = 8.9
            self.voltage_level = 400000
            self.max_num_conductors = 4

            self.flag_range_input[0] = self.check_elements_in_range([self.current_y1_line, self.current_y2_line, self.current_y3_line], self.min_ph_line_height, self.max_ph_line_height)
            self.flag_range_input[1] = self.check_elements_in_range([self.current_x1_line], -self.max_hor_distance, -self.min_hor_distance)
            self.flag_range_input[2] = self.check_elements_in_range([abs(self.current_x2_line)], 0, self.max_hor_distance_center)
            self.flag_range_input[3] = self.check_elements_in_range([self.current_x3_line], self.min_hor_distance, self.max_hor_distance)

        elif self.current_tower_type == 2:
            self.max_ph_line_height = 48.8
            self.min_ph_line_height = 36
            self.max_hor_distance = 5.35
            self.min_hor_distance = 1.8
            self.voltage_level = 154000
            self.max_num_conductors = 3

            self.flag_range_input[0] = self.check_elements_in_range([self.current_y1_line, self.current_y2_line, self.current_y3_line], self.min_ph_line_height, self.max_ph_line_height)
            self.flag_range_input[1] = self.check_elements_in_range([self.current_x1_line, self.current_x2_line, self.current_x3_line], self.min_hor_distance, self.max_hor_distance)

        
        if self.current_conductor_type == 0:
            self.diameter = 21.793
            self.conductor_gmr = 8.809
            self.ac_resistance = 0.132
            self.current_capacity = 659

        elif self.current_conductor_type == 1:
            self.diameter = 28.143
            self.conductor_gmr = 11.369
            self.ac_resistance = 0.080
            self.current_capacity = 907

        elif self.current_conductor_type == 2:
            self.diameter = 30.378
            self.conductor_gmr = 12.253
            self.ac_resistance = 0.067
            self.current_capacity = 996

        elif self.current_conductor_type == 3:
            self.diameter = 29.591
            self.conductor_gmr = 11.765
            self.ac_resistance = 0.068
            self.current_capacity = 993

        elif self.current_conductor_type == 4:
            self.diameter = 35.103
            self.conductor_gmr = 14.204
            self.ac_resistance = 0.051
            self.current_capacity = 1187


        if self.current_number_of_circuits == 1:
            distance_between_bundles_12 = ((self.current_x1_line - self.current_x2_line) ** 2 + (self.current_y1_line - self.current_y2_line) ** 2) ** (1 / 2)
            distance_between_bundles_23 = ((self.current_x3_line - self.current_x2_line) ** 2 + (self.current_y3_line - self.current_y2_line) ** 2) ** (1 / 2)
            distance_between_bundles_13 = ((self.current_x3_line - self.current_x1_line) ** 2 + (self.current_y3_line - self.current_y1_line) ** 2) ** (1 / 2)
            self.current_gmd = (distance_between_bundles_12 * distance_between_bundles_23 * distance_between_bundles_13) ** (1 / 3)

        elif self.current_number_of_circuits == 2:
            self.current_x4_line = -self.current_x1_line
            self.current_x5_line = -self.current_x2_line
            self.current_x6_line = -self.current_x3_line

            self.distance_between_bundles_12 = ((self.current_x1_line - self.current_x2_line) ** 2 + (self.current_y1_line - self.current_y2_line) ** 2) ** (1 / 2)
            self.distance_between_bundles_15 = ((self.current_x1_line - self.current_x5_line) ** 2 + (self.current_y1_line - self.current_y2_line) ** 2) ** (1 / 2)
            self.distance_between_bundles_62 = ((self.current_x6_line - self.current_x2_line) ** 2 + (self.current_y3_line - self.current_y2_line) ** 2) ** (1 / 2)
            self.distance_between_bundles_65 = ((self.current_x6_line - self.current_x5_line) ** 2 + (self.current_y3_line - self.current_y2_line) ** 2) ** (1 / 2)
            self.distance_ab = (self.distance_between_bundles_12 * self.distance_between_bundles_15 * self.distance_between_bundles_62 * self.distance_between_bundles_65) ** (1 / 4)

            self.distance_between_bundles_13 = ((self.current_x1_line - self.current_x3_line) ** 2 + (self.current_y1_line - self.current_y3_line) ** 2) ** (1 / 2)
            self.distance_between_bundles_14 = ((self.current_x1_line - self.current_x4_line) ** 2 + (self.current_y1_line - self.current_y1_line) ** 2) ** (1 / 2)
            self.distance_between_bundles_64 = ((self.current_x6_line - self.current_x4_line) ** 2 + (self.current_y3_line - self.current_y1_line) ** 2) ** (1 / 2)
            self.distance_between_bundles_63 = ((self.current_x6_line - self.current_x3_line) ** 2 + (self.current_y3_line - self.current_y3_line) ** 2) ** (1 / 2)
            self.distance_ac = (self.distance_between_bundles_13 * self.distance_between_bundles_14 * self.distance_between_bundles_64 * self.distance_between_bundles_63) ** (1 / 4)

            self.distance_between_bundles_24 = ((self.current_x2_line - self.current_x4_line) ** 2 + (self.current_y2_line - self.current_y1_line) ** 2) ** (1 / 2)
            self.distance_between_bundles_23 = ((self.current_x2_line - self.current_x3_line) ** 2 + (self.current_y2_line - self.current_y3_line) ** 2) ** (1 / 2)
            self.distance_between_bundles_53 = ((self.current_x5_line - self.current_x3_line) ** 2 + (self.current_y2_line - self.current_y3_line) ** 2) ** (1 / 2)
            self.distance_between_bundles_54 = ((self.current_x5_line - self.current_x4_line) ** 2 + (self.current_y2_line - self.current_y1_line) ** 2) ** (1 / 2)
            self.distance_bc = (self.distance_between_bundles_24 * self.distance_between_bundles_23 * self.distance_between_bundles_53 * self.distance_between_bundles_54) ** (1 / 4)

            self.current_gmd = (self.distance_ab * self.distance_ac * self.distance_bc) ** (1/3)
        
        self.radius_of_conductor = self.diameter / 2

        if self.current_number_of_conductors == 1:
            self.current_gmr = self.conductor_gmr
            self.radius_of_bundle = self.radius_of_conductor
        elif self.current_number_of_conductors == 2:
            self.current_gmr = (self.conductor_gmr * self.current_distance_between_conductors) ** (1 / 2)
            self.radius_of_bundle = (self.radius_of_conductor * self.current_distance_between_conductors) ** (1 / 2)
        elif self.current_number_of_conductors == 3:
            self.current_gmr = (self.conductor_gmr * self.current_distance_between_conductors ** 2) ** (1 / 3)
            self.radius_of_bundle = (self.radius_of_conductor * self.current_distance_between_conductors ** 2) ** (1 / 3)
        elif self.current_number_of_conductors == 4:
            self.current_gmr = (self.conductor_gmr * (self.current_distance_between_conductors ** 3) * (2 ** (1 / 2))) ** (1 / 4)
            self.radius_of_bundle = (self.radius_of_conductor * (self.current_distance_between_conductors ** 3) * (2 ** (1 / 2))) ** (1 / 4)

        if self.current_number_of_circuits == 1:
         self.inductance_per_distance = 2 * 10 ** (-7) * math.log(self.current_gmd / self.current_gmr * (10 ** 3))
         self.inductance = self.inductance_per_distance * self.current_length_of_tl * 1000 * 1000
         self.capacitance_per_distance = 2 * math.pi * (8.8541878128 * (10 ** -12)) / (math.log(self.current_gmd / self.radius_of_bundle * (10 ** 3)))
         self.capacitance = self.capacitance_per_distance * self.current_length_of_tl * 1000 * 1000000
        elif  self.current_number_of_circuits == 2:
            self.dista = ((self.current_x1_line - self.current_x6_line) ** 2 + (self.current_y1_line - self.current_y3_line) ** 2) ** (1 / 2)
            self.distb = ((self.current_x2_line - self.current_x5_line) ** 2 + (self.current_y2_line - self.current_y2_line) ** 2) ** (1 / 2)
            self.distc = ((self.current_x3_line - self.current_x4_line) ** 2 + (self.current_y3_line - self.current_y1_line) ** 2) ** (1 / 2)
            self.doublegmra= (self.dista*(self.current_gmr*10**(-3)))**(1/2)
            self.doublegmrb = (self.distb* (self.current_gmr*10**(-3))) ** (1 / 2)
            self.doublegmrc = (self.distc *(self.current_gmr*10**(-3))) ** (1 / 2)
            self.new_gmr = (self.doublegmra*self.doublegmrb*self.doublegmrc)**(1/3)
            self.doublereqa = (self.dista * (self.radius_of_bundle*10**(-3))) ** (1 / 2)
            self.doublereqb = (self.distb * (self.radius_of_bundle*10**(-3))) ** (1 / 2)
            self.doublereqc = (self.distc * (self.radius_of_bundle*10**(-3))) ** (1 / 2)
            self.new_rad_bund = (self.doublereqa * self.doublereqb * self.doublereqc) ** (1 / 3)
            self.inductance_per_distance = 2 * 10 ** (-7) * math.log(self.current_gmd / self.new_gmr )
            self.inductance = self.inductance_per_distance * self.current_length_of_tl * 1000 * 1000
            self.capacitance_per_distance = 2 * math.pi * (8.8541878128 * (10 ** -12)) / (math.log(self.current_gmd / self.new_rad_bund))
            self.capacitance = self.capacitance_per_distance * self.current_length_of_tl * 1000 * 1000000

            

        self.resistance = self.ac_resistance*self.current_length_of_tl/self.current_number_of_conductors/self.current_number_of_circuits
        self.line_capacity = self.current_number_of_circuits*self.current_number_of_conductors*math.sqrt(3)*self.current_capacity*self.voltage_level/1000000
            
        if 1 in self.flag_blank_input:         
            dlg1 = QMessageBox(self)
            dlg1.setWindowTitle("Blank Input")
            dlg1.setText("Please check the inputs! \n-There is at least 1 missing parameter that is not filled at all")
            dlg1.exec()

        elif 1 in self.flag_wrong_input:
            dlg2 = QMessageBox(self)
            dlg2.setWindowTitle("Wrong Input")
            dlg2.setText("Please check the inputs! \n-The inputs must be entered as numbers in decimal. \n-The inputs cannot include any character or any special character.")
            dlg2.exec()
        
        elif 1 in self.flag_range_input:
            dlg3 = QMessageBox(self)
            dlg3.setWindowTitle("Calculated Parameters")
            dlg3.setText("Check the range of the inputs! \n-There is at least 1 parameter that is out of range.")
            dlg3.exec()

        else:
            dlg4 = QMessageBox(self)
            dlg4.setWindowTitle("Calculated Parameters")
            dlg4.setText("R={} {} \nL={} mH \nC={} {}F \nLine Capacity={} MVA".format(self.resistance, chr(937), self.inductance, self.capacitance, chr(956), self.line_capacity))
            dlg4.exec()

    def tower_type_changed(self, index):
        self.current_tower_type=index

        if self.current_tower_type == 0:
            self.number_of_circuits.removeItem(1)
            self.number_of_conductors.removeItem(3)
            self.tower_image.setPixmap(QPixmap('narrow_base_tower.png'))
        
        elif self.current_tower_type == 1:
            self.number_of_circuits.removeItem(1)
            self.number_of_conductors.addItem("4")
            self.tower_image.setPixmap(QPixmap('delta_tower.png'))

        elif self.current_tower_type == 2:
            self.number_of_circuits.addItem("2")
            self.number_of_conductors.removeItem(3)
            self.tower_image.setPixmap(QPixmap('vertical_tower.png'))      

    def number_of_circuits_changed(self,index):
        self.current_number_of_circuits=index+1

    def x1_line_changed(self, text):
        self.flag_blank_input[0] = self.check_blank(text)
        self.flag_wrong_input[0] = self.check_wrong(text)
        if not(self.flag_wrong_input[0]):
            self.current_x1_line = float(text)
            
    def y1_line_changed(self, text):
        self.flag_blank_input[1] = self.check_blank(text)
        self.flag_wrong_input[1] = self.check_wrong(text)
        if not(self.flag_wrong_input[1]):
            self.current_y1_line = float(text)
        
    def x2_line_changed(self, text):
        self.flag_blank_input[2] = self.check_blank(text)
        self.flag_wrong_input[2] = self.check_wrong(text)
        if not(self.flag_wrong_input[2]):
            self.current_x2_line = float(text)
        
    def y2_line_changed(self, text):
        self.flag_blank_input[3] = self.check_blank(text)
        self.flag_wrong_input[3] = self.check_wrong(text)
        if not(self.flag_wrong_input[3]):
            self.current_y2_line = float(text)
        
    def x3_line_changed(self, text):
        self.flag_blank_input[4] = self.check_blank(text)
        self.flag_wrong_input[4] = self.check_wrong(text)
        if not(self.flag_wrong_input[4]):
            self.current_x3_line = float(text)
        
    def y3_line_changed(self, text):
        self.flag_blank_input[5] = self.check_blank(text)
        self.flag_wrong_input[5] = self.check_wrong(text)
        if not(self.flag_wrong_input[5]):
            self.current_y3_line = float(text)
    
    def distance_between_conductors_changed(self, text):
        self.flag_blank_input[6] = self.check_blank(text)
        self.flag_wrong_input[6] = self.check_wrong(text)
        if not(self.flag_wrong_input[6]):
            self.current_distance_between_conductors = float(text)

    def number_of_conductors_changed(self, index):
        self.current_number_of_conductors=index+1

    def conductor_type_changed(self, index):
        self.current_conductor_type=index

    def length_of_tl_changed(self, text):
        self.flag_blank_input[7] = self.check_blank(text)
        self.flag_wrong_input[7] = self.check_wrong(text)
        if not(self.flag_wrong_input[7]):
            self.current_length_of_tl = float(text)

    def check_blank(self, text):
        if str.strip(text) == "":
            return 1
        else:
            return 0
    
    def check_wrong(self, text):
        try:
            float(text)
            return 0
        except ValueError:
            return 1
    
    def check_elements_in_range(self, lst, min_value, max_value):
        return not(all(min_value <= element <= max_value for element in lst))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
