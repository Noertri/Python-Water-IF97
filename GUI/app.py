import tkinter as tk
import math
from tkinter import messagebox, ttk
from IF97 import if97


class PyWater(tk.Tk):

    menuVal = ("T-x", "P-x", "P-T")
    pressUnit = ("bar", "Pa", "KPa", "MPa")
    tempUnit = ("C", "K")
    xUnit = ("",)

    def __init__(self):
        super().__init__()
        self.title("PyWater")

        #variables
        self.label2Val = tk.StringVar(value="P")
        self.label3Val = tk.StringVar(value="T")
        self.menuVar = tk.StringVar()
        self.unit1Var = tk.StringVar()
        self.unit2Var = tk.StringVar()
        self.input1Var = tk.DoubleVar()
        self.input2Var = tk.DoubleVar()
        self.output1Var = tk.DoubleVar()
        self.output2Var = tk.DoubleVar()
        self.output3Var = tk.DoubleVar()
        self.output4Var = tk.DoubleVar()
        self.output5Var = tk.DoubleVar()
        self.output6Var = tk.DoubleVar()
        self.output7Var = tk.DoubleVar()
        self.output8Var = tk.DoubleVar()
        self.output9Var = tk.DoubleVar()

        #frames
        self.inputs_frame = ttk.Frame(self, padding=(5, 5, 5, 5), width=300)
        self.buttons_frame = ttk.Frame(self, padding=(5, 5, 5, 5), width=300)
        self.outputs_frame = ttk.Frame(self, padding=(5, 5, 5, 5), width=300)
        self.inputs_frame.grid(row=0, column=0, padx=12, pady=(12, 0))
        self.buttons_frame.grid(row=1, column=0, padx=12, pady=12)
        self.outputs_frame.grid(row=2, column=0, padx=12, pady=(0, 12))

        #labels
        self.label1 = ttk.Label(self.inputs_frame, text="Fungsi", justify="left", width=8)
        self.label2 = ttk.Label(self.inputs_frame, textvariable=self.label2Val, justify="left", width=8)
        self.label3 = ttk.Label(self.inputs_frame, textvariable=self.label3Val, justify="left", width=8)
        self.label4 = ttk.Label(self.outputs_frame, text="Psat", justify="left", width=8)
        self.label5 = ttk.Label(self.outputs_frame, text="Tsat", justify="left", width=8)
        self.label6 = ttk.Label(self.outputs_frame, text="v", justify="left", width=8)
        self.label7 = ttk.Label(self.outputs_frame, text="u", justify="left", width=8)
        self.label8 = ttk.Label(self.outputs_frame, text="h", justify="left", width=8)
        self.label9 = ttk.Label(self.outputs_frame, text="s", justify="left", width=8)
        self.label10 = ttk.Label(self.outputs_frame, text="Cv", justify="left", width=8)
        self.label11 = ttk.Label(self.outputs_frame, text="Cp", justify="left", width=8)
        # self.label12 = ttk.Label(self.outputs_frame, text="x", justify="left", width=8)
        self.label13 = ttk.Label(self.outputs_frame, text="KPa", justify="left", width=8)
        self.label14 = ttk.Label(self.outputs_frame, text="K", justify="left", width=8)
        self.label15 = ttk.Label(self.outputs_frame, text="m^3/Kg", justify="left", width=8)
        self.label16 = ttk.Label(self.outputs_frame, text="KJ/Kg", justify="left", width=8)
        self.label17 = ttk.Label(self.outputs_frame, text="KJ/Kg", justify="left", width=8)
        self.label18 = ttk.Label(self.outputs_frame, text="KJ/Kg*K", justify="left", width=8)
        self.label19 = ttk.Label(self.outputs_frame, text="KJ/Kg*K", justify="left", width=8)
        self.label20 = ttk.Label(self.outputs_frame, text="KJ/Kg*K", justify="left", width=8)
        # self.label21 = ttk.Label(self.outputs_frame, text="")
        self.credit = ttk.Label(self, text="Created by:\nNoertri\ntrinuruns@gmail.com", justify="center")
        self.credit.grid(row=12, column=0, pady=(0, 12))
        self.label1.grid(row=0, column=0, pady=(0, 5))
        self.label2.grid(row=1, column=0, pady=(0, 5))
        self.label3.grid(row=2, column=0, pady=(0, 5))
        # self.label4.grid(row=4, column=0, pady=(0, 5))
        self.label4.grid_forget()
        # self.label5.grid(row=5, column=0, pady=(0, 5))
        self.label5.grid_forget()
        self.label6.grid(row=6, column=0, pady=(0, 5))
        self.label7.grid(row=7, column=0, pady=(0, 5))
        self.label8.grid(row=8, column=0, pady=(0, 5))
        self.label9.grid(row=9, column=0, pady=(0, 5))
        self.label10.grid(row=10, column=0, pady=(0, 5))
        self.label11.grid(row=11, column=0, pady=(0, 5))
        # self.label12.grid(row=12, column=0, pady=(0, 5))
        # self.label13.grid(row=4, column=2, pady=(0, 5))
        self.label13.grid_forget()
        # self.label14.grid(row=5, column=2, pady=(0, 5))
        self.label14.grid_forget()
        self.label15.grid(row=6, column=2, pady=(0, 5))
        self.label16.grid(row=7, column=2, pady=(0, 5))
        self.label17.grid(row=8, column=2, pady=(0, 5))
        self.label18.grid(row=9, column=2, pady=(0, 5))
        self.label19.grid(row=10, column=2, pady=(0, 5))
        self.label20.grid(row=11, column=2, pady=(0, 5))
        # self.label21.grid(row=12, column=2, pady=(0, 5))

        #comboboxes
        self.menu = ttk.Combobox(self.inputs_frame, width=14, state="readonly", textvariable=self.menuVar)
        self.menu["values"] = self.menuVal
        self.menu.current(2)
        self.menu.bind("<<ComboboxSelected>>", self.combo1_callback)
        self.unit1 = ttk.Combobox(self.inputs_frame, width=5, state="readonly", textvariable=self.unit1Var)
        self.unit1["values"] = self.pressUnit
        self.unit1.current(2)
        self.unit2 = ttk.Combobox(self.inputs_frame, width=5, state="readonly", textvariable=self.unit2Var)
        self.unit2["values"] = self.tempUnit
        self.unit2.current(1)
        self.menu.grid(column=1, row=0, sticky="nw", padx=5, pady=(0, 5))
        self.unit1.grid(column=2, row=1, sticky="nw", pady=(0, 5))
        self.unit2.grid(column=2, row=2, sticky="nw", pady=(0, 5))

        #entryboxes
        self.input1 = ttk.Entry(self.inputs_frame, width=16, textvariable=self.input1Var)
        self.input2 = ttk.Entry(self.inputs_frame, width=16, textvariable=self.input2Var)
        self.output1 = ttk.Entry(self.outputs_frame, width=16, state="readonly", textvariable=self.output1Var)
        self.output2 = ttk.Entry(self.outputs_frame, width=16, state="readonly", textvariable=self.output2Var)
        self.output3 = ttk.Entry(self.outputs_frame, width=16, state="readonly", textvariable=self.output3Var)
        self.output4 = ttk.Entry(self.outputs_frame, width=16, state="readonly", textvariable=self.output4Var)
        self.output5 = ttk.Entry(self.outputs_frame, width=16, state="readonly", textvariable=self.output5Var)
        self.output6 = ttk.Entry(self.outputs_frame, width=16, state="readonly", textvariable=self.output6Var)
        self.output7 = ttk.Entry(self.outputs_frame, width=16, state="readonly", textvariable=self.output7Var)
        self.output8 = ttk.Entry(self.outputs_frame, width=16, state="readonly", textvariable=self.output8Var)
        self.output9 = ttk.Entry(self.outputs_frame, width=16, state="readonly", textvariable=self.output9Var)
        self.input1.grid(row=1, column=1, padx=5, pady=(0, 5))
        self.input2.grid(row=2, column=1, padx=5, pady=(0, 5))
        # self.output1.grid(row=4, column=1, padx=5, pady=(0, 5))
        self.output1.grid_forget()
        # self.output2.grid(row=5, column=1, padx=5, pady=(0, 5))
        self.output2.grid_forget()
        self.output3.grid(row=6, column=1, padx=5, pady=(0, 5))
        self.output4.grid(row=7, column=1, padx=5, pady=(0, 5))
        self.output5.grid(row=8, column=1, padx=5, pady=(0, 5))
        self.output6.grid(row=9, column=1, padx=5, pady=(0, 5))
        self.output7.grid(row=10, column=1, padx=5, pady=(0, 5))
        self.output8.grid(row=11, column=1, padx=5, pady=(0, 5))
        # self.output9.grid(row=12, column=1, padx=5, pady=(0, 5))

        #buttons
        self.btn1 = ttk.Button(self.buttons_frame, text="Calc", command=self.btn1_callback)
        self.btn2 = ttk.Button(self.buttons_frame, text="Reset", command=self.btn2_callback)
        self.btn1.grid(column=0, row=3, padx=10)
        self.btn2.grid(column=1, row=3, padx=10)

        self.resizable(False, False)
        self.mainloop()

    def combo1_callback(self, event=None):

        match self.menuVar.get():
            case "T-x":
                self.label2Val.set("Tsat")
                self.label3Val.set("x")
                self.unit1["values"] = self.tempUnit
                self.unit1.current(1)
                self.unit2["values"] = self.xUnit
                self.unit2.current(0)
                self.label4.grid(row=4, column=0, pady=(0, 5))
                self.label5.grid(row=5, column=0, pady=(0, 5))
                self.output1.grid(row=4, column=1, padx=5, pady=(0, 5))
                self.output2.grid(row=5, column=1, padx=5, pady=(0, 5))
                self.label13.grid(row=4, column=2, pady=(0, 5))
                self.label14.grid(row=5, column=2, pady=(0, 5))
            case "P-x":
                self.label2Val.set("Psat")
                self.label3Val.set("x")
                self.unit1["values"] = self.pressUnit
                self.unit1.current(2)
                self.unit2["values"] = self.xUnit
                self.unit2.current(0)
                self.label4.grid(row=4, column=0, pady=(0, 5))
                self.label5.grid(row=5, column=0, pady=(0, 5))
                self.output1.grid(row=4, column=1, padx=5, pady=(0, 5))
                self.output2.grid(row=5, column=1, padx=5, pady=(0, 5))
                self.label13.grid(row=4, column=2, pady=(0, 5))
                self.label14.grid(row=5, column=2, pady=(0, 5))
            case "P-T":
                self.label2Val.set("P")
                self.label3Val.set("T")
                self.unit1["values"] = self.pressUnit
                self.unit1.current(2)
                self.unit2["values"] = self.tempUnit
                self.unit2.current(1)
                self.label4.grid_forget()
                self.label5.grid_forget()
                self.output1.grid_forget()
                self.output2.grid_forget()
                self.label13.grid_forget()
                self.label14.grid_forget()
            case _:
                self.menuVar.set(self.menuVal[0])

    def btn1_callback(self):
        try:
            if self.menuVar.get() == self.menuVal[0] and (tsat := self._convertT(self.input1Var.get(), self.unit1Var.get())) is not None and (x := self.input2Var.get()) is not None and (ans := if97(t=tsat, x=x)):
                self.output1Var.set(round(ans['psat'], 9))
                self.output2Var.set(round(ans['tsat'], 9))
                self.output3Var.set(round(ans['v'], 9))
                self.output4Var.set(round(ans['u'], 9))
                self.output5Var.set(round(ans['h'], 9))
                self.output6Var.set(round(ans['s'], 9))
                if ans["cp"] is not None and ans["cv"] is not None:
                    self.output7Var.set(round(ans['cp'], 9))
                    self.output8Var.set(round(ans['cv'], 9))
                else:
                    self.output7Var.set(math.inf)
                    self.output8Var.set(math.inf)
            elif self.menuVar.get() == self.menuVal[1] and (psat := self._convertP(self.input1Var.get(), self.unit1Var.get())) is not None and (x := self.input2Var.get()) is not None and (ans := if97(p=psat, x=x)) is not None:
                self.output1Var.set(round(ans['psat'], 9))
                self.output2Var.set(round(ans['tsat'], 9))
                self.output3Var.set(round(ans['v'], 9))
                self.output4Var.set(round(ans['u'], 9))
                self.output5Var.set(round(ans['h'], 9))
                self.output6Var.set(round(ans['s'], 9))
                if ans["cp"] is not None and ans["cv"] is not None:
                    self.output7Var.set(round(ans['cp'], 9))
                    self.output8Var.set(round(ans['cv'], 9))
                else:
                    self.output7Var.set(math.inf)
                    self.output8Var.set(math.inf)
            elif self.menuVar.get() == self.menuVal[2] and (p := self._convertP(self.input1Var.get(), self.unit1Var.get())) is not None and (t := self._convertT(self.input2Var.get(), self.unit2Var.get())) is not None and (ans := if97(p=p, t=t)) is not None:
                self.output3Var.set(round(ans['v'], 9))
                self.output4Var.set(round(ans['u'], 9))
                self.output5Var.set(round(ans['h'], 9))
                self.output6Var.set(round(ans['s'], 9))
                self.output7Var.set(round(ans['cp'], 9))
                self.output8Var.set(round(ans['cv'], 9))
        except Exception as e:
            messagebox.showerror(title="Value Error!!!", message=e)

    def btn2_callback(self):
        self.input1Var.set(0.)
        self.input2Var.set(0.)
        self.output1Var.set(0.)
        self.output2Var.set(0.)
        self.output3Var.set(0.)
        self.output4Var.set(0.)
        self.output5Var.set(0.)
        self.output6Var.set(0.)
        self.output7Var.set(0.)
        self.output8Var.set(0.)

    @staticmethod
    def _convertT(value, unit):
        if value is not None and unit is not None:
            match unit:
                case "C":
                    value += 273.15
                    return value
                case "K":
                    return value
                case _:
                    return None
        else:
            return None

    @staticmethod
    def _convertP(value, unit):
        if value is not None and unit is not None:
            match unit:
                case "bar":
                    return value*100
                case "Pa":
                    return value/1000
                case "KPa":
                    return value
                case "MPa":
                    return value*1000
                case _:
                    return None
        else:
            return None


if __name__ == "__main__":
    ui = PyWater()