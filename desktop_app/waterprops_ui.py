from iapws95 import *
import math
import tkinter as tk
from tkinter import ttk
from tkinter import font


class _Frame():

    def create(self, tab=None):
        frame0 = ttk.Frame(tab, padding=(30, 20, 30, 30), borderwidth=1, relief="solid", width=300, height=150)
        frame1 = ttk.Frame(tab, padding=(10, 10, 10, 10), width=300, height=50)
        frame2 = ttk.Frame(tab, borderwidth=1, relief="solid", padding=(5, 5, 5, 5), width=300, height=200)
        frame0.grid(row=0, column=0, sticky="WE")
        frame1.grid(row=3, column=0, sticky="WE")
        frame2.grid(row=4, column=0, sticky="WE")
        return frame0, frame1, frame2


_frame = _Frame()


class WaterPropUi(tk.Tk):

    def __init__(self):

        #Inisialisasi
        super().__init__()
        self.props = dict()
        self.props["saturation"] = list()
        self.props["singlephase"] = list()

        #Variabel combobox
        self.menu0 = tk.StringVar()
        self.menu2 = tk.StringVar()
        self.menu3 = tk.StringVar()

        #satuan input
        self.unit1 = tk.StringVar()
        self.unit2 = tk.StringVar()
        self.unit3 = tk.StringVar()
        self.unit4 = tk.StringVar()

        #input entrybox
        self.input1 = tk.StringVar()
        self.input2 = tk.StringVar()
        self.input3 = tk.StringVar()
        self.input4 = tk.StringVar()
        self.input5 = tk.StringVar()

        #label yang dimanipulasi
        self.cbb2 = None
        self.cbb3 = None
        self.cols = dict()
        self.cols["frame02"] = list()
        self.cols["frame12"] = list()

        self.title("Water Properties")
        self.resizable(False, False)

        #Tab
        self.tabcontrol = ttk.Notebook(self, padding=(5, 5, 5, 5))
        self.tab0 = ttk.Frame(self.tabcontrol, padding=(15, 20, 15, 15))
        self.tab1 = ttk.Frame(self.tabcontrol, padding=(15, 15, 15, 15))
        self.tabcontrol.add(self.tab0, text="Saturasi")
        self.tabcontrol.add(self.tab1, text="Satu Fase")
        self.tabcontrol.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))

        #Frames
        self.frame00, self.frame01, self.frame02 = _frame.create(tab=self.tab0)
        self.frame10, self.frame11, self.frame12 = _frame.create(tab=self.tab1)

        self.func_tab0()
        self.func_tab1()

        self.mainloop()

    def func_tab0(self):
        lbl1 = ttk.Label(self.frame00, text="SATURASI", font=font.Font(size=16), justify="center")
        cbb1 = ttk.Combobox(self.frame00, width=3, values=("T", "P"), textvariable=self.menu0, font=font.Font(
                size=10), state="readonly")
        entri1 = ttk.Entry(self.frame00, width=18, textvariable=self.input1)
        lbl2 = ttk.Label(self.frame00, text="X", justify="left", font=font.Font(size=10))
        entri2 = ttk.Entry(self.frame00, width=18, textvariable=self.input2)
        self.cbb3 = ttk.Combobox(self.frame00, values=("%", "-"), width=4, textvariable=self.unit2, font=font.Font(
                size=10), state="readonly")
        btn1 = ttk.Button(self.frame01, text="Hitung", command=self.func_btn1)
        cls1 = ttk.Button(self.frame01, text="Reset", command=self.fun_cls1)

        self.cbb2 = ttk.Combobox(self.frame00, width=4, textvariable=self.unit1, font=font.Font(size=10),
                                 state="readonly")

        cbb1.current(0)
        self.cbb3.current(0)

        self.func_cbb1()
        cbb1.bind("<<ComboboxSelected>>", self.func_cbb1)

        lbl1.grid(row=0, column=1, pady=(0, 20), sticky="nw")
        cbb1.grid(column=0, row=1, padx=(0, 10), sticky="nw")
        entri1.grid(column=1, row=1, padx=(0, 10), pady=(0, 20), sticky="nw")
        self.cbb2.grid(column=2, row=1, pady=(0, 20), sticky="nw")
        lbl2.grid(column=0, row=2, sticky="nw")
        entri2.grid(column=1, row=2, sticky="nw")
        self.cbb3.grid(column=2, row=2, sticky="nw")
        btn1.grid(column=0, row=3, padx=(20, 100))
        cls1.grid(column=2, row=3, padx=(0, 20))

    def func_cbb1(self, event=None):

        if self.menu0.get() == "P":
            self.cbb2["values"] = ("Pa", "KPa", "MPa")
            self.cbb2.current(1)

        elif self.menu0.get() == "T":
            self.cbb2["values"] = ("C", "K")
            self.cbb2.current(0)

    def temp_converter(self, value, unit):

        if unit.get() == "C":
            ans = float(value.get()) + 273.15
            return ans
        else:
            return float(value.get())

    def press_converter(self, value, unit):

        if unit.get() == "Pa":
            return float(value.get())/1000
        elif unit.get() == "MPa":
            return float(value.get())*1000
        else:
            return float(value.get())

    def func_btn1(self, event=None):
        ans = dict()
        psat, tsat, x = [math.nan for _ in range(3)]
        units = ["MPa", "K", "Kg/m³", "m³/Kg", "KJ/Kg", "KJ/Kg", "KJ/Kg", "KJ/Kg*K", "KJ/Kg*K"]
        outs = ["Tekanan",
                "Suhu",
                "Massa jenis",
                "Volume jenis",
                "Entropi",
                "Entalpi",
                "Energi dalam",
                "Cp",
                "Cv"]
        for idx in outs:
            ans[idx] = math.nan

        if self.menu0.get() == "P":
            if (self.input1.get() != "") and (self.input2.get() != ""):
                psat = self.press_converter(value=self.input1, unit=self.unit1)
                if self.unit2.get() == "%":
                    x = float(self.input2.get())/100
                elif self.unit2.get() == "-":
                    x = float(self.input2.get())

                if (not math.isnan(psat)) and (x >= 0) and (x <= 1):
                    if (psat > PRESST) and (psat <= PRESSC):
                        tsat = water95(Psat=psat, X=x, desc="Tsat")
                        ans["Tekanan"] = float(self.input1.get())/1000
                        ans["Suhu"] = round(tsat, 8)
                        ans["Massa jenis"] = round(water95(Psat=psat, X=x, desc="rho"), 8)
                        ans["Volume jenis"] = round(water95(Psat=psat, X=x, desc="v"), 8)
                        ans["Entropi"] = round(water95(Psat=psat, X=x, desc="s"), 8)
                        ans["Entalpi"] = round(water95(Psat=psat, X=x, desc="h"), 8)
                        ans["Energi dalam"] = round(water95(Psat=psat, X=x, desc="u"), 8)
                        ans["Cp"] = round(water95(Psat=psat, X=x, desc="Cp"), 8)
                        ans["Cv"] = round(water95(Psat=psat, X=x, desc="Cv"), 8)
                        units[0] = "MPa"
                        units[1] = "K"
                    elif math.isclose(psat, PRESST, abs_tol=1e-6):
                        tsat = water95(Psat=psat, X=x, desc="Tsat")
                        ans["Tekanan"] = float(self.input1.get())/1000
                        ans["Suhu"] = round(tsat, 8)
                        ans["Massa jenis"] = round(water95(Psat=psat, X=x, desc="rho"), 8)
                        ans["Volume jenis"] = round(water95(Psat=psat, X=x, desc="v"), 8)
                        ans["Entropi"] = round(water95(Psat=psat, X=x, desc="s"), 8)
                        ans["Entalpi"] = round(water95(Psat=psat, X=x, desc="h"), 8)
                        ans["Energi dalam"] = round(water95(Psat=psat, X=x, desc="u"), 8)
                        ans["Cp"] = round(water95(Psat=psat, X=x, desc="Cp"), 8)
                        ans["Cv"] = round(water95(Psat=psat, X=x, desc="Cv"), 8)
                        units[0] = "MPa"
                        units[1] = "K"
                    else:
                        ans["Tekanan"] = float(self.input1.get())/1000
                        ans["Massa jenis"] = round(water95(Psat=psat, X=x, desc="rho"), 8)
                        ans["Volume jenis"] = round(water95(Psat=psat, X=x, desc="v"), 8)
                        ans["Entropi"] = round(water95(Psat=psat, X=x, desc="s"), 8)
                        ans["Entalpi"] = round(water95(Psat=psat, X=x, desc="h"), 8)
                        ans["Energi dalam"] = round(water95(Psat=psat, X=x, desc="u"), 8)
                        ans["Cp"] = round(water95(Psat=psat, X=x, desc="Cp"), 8)
                        ans["Cv"] = round(water95(Psat=psat, X=x, desc="Cv"), 8)
                        units[0] = "MPa"
                        units[1] = "K"

        elif self.menu0.get() == "T":
            if (self.input1.get() != "") and (self.input2.get() != ""):
                tsat = self.temp_converter(value=self.input1, unit=self.unit1)
                if self.unit2.get() == "%":
                    x = float(self.input2.get())/100
                elif self.unit2.get() == "-":
                    x = float(self.input2.get())

                if (not math.isnan(tsat)) and (x >= 0) and (x <= 1):
                    if (tsat > 273.15) and (tsat < TEMPC):
                        psat = water95(Tsat=tsat, X=x, desc="Psat")
                        ans["Tekanan"] = round(psat/1000, 8)
                        ans["Suhu"] = float(self.input1.get())
                        ans["Massa jenis"] = round(water95(Psat=psat, X=x, desc="rho"), 8)
                        ans["Volume jenis"] = round(water95(Psat=psat, X=x, desc="v"), 8)
                        ans["Entropi"] = round(water95(Psat=psat, X=x, desc="s"), 8)
                        ans["Entalpi"] = round(water95(Psat=psat, X=x, desc="h"), 8)
                        ans["Energi dalam"] = round(water95(Psat=psat, X=x, desc="u"), 8)
                        ans["Cp"] = round(water95(Psat=psat, X=x, desc="Cp"), 8)
                        ans["Cv"] = round(water95(Psat=psat, X=x, desc="Cv"), 8)
                        units[0] = "MPa"
                        units[1] = self.unit1.get()
                    elif math.isclose(tsat, TEMPC, abs_tol=1e-3):
                        psat = water95(Tsat=tsat, X=x, desc="Psat")
                        ans["Tekanan"] = round(psat, 8)
                        ans["Suhu"] = float(self.input1.get())
                        ans["Massa jenis"] = round(water95(Psat=psat, X=x, desc="rho"), 8)
                        ans["Volume jenis"] = round(water95(Psat=psat, X=x, desc="v"), 8)
                        ans["Entropi"] = round(water95(Psat=psat, X=x, desc="s"), 8)
                        ans["Entalpi"] = round(water95(Psat=psat, X=x, desc="h"), 8)
                        ans["Energi dalam"] = round(water95(Psat=psat, X=x, desc="u"), 8)
                        ans["Cp"] = round(water95(Psat=psat, X=x, desc="Cp"), 8)
                        ans["Cv"] = round(water95(Psat=psat, X=x, desc="Cv"), 8)
                        units[0] = "MPa"
                        units[1] = self.unit1.get()
                    else:
                        ans["Suhu"] = float(self.input1.get())
                        ans["Massa jenis"] = round(water95(Psat=psat, X=x, desc="rho"), 8)
                        ans["Volume jenis"] = round(water95(Psat=psat, X=x, desc="v"), 8)
                        ans["Entropi"] = round(water95(Psat=psat, X=x, desc="s"), 8)
                        ans["Entalpi"] = round(water95(Psat=psat, X=x, desc="h"), 8)
                        ans["Energi dalam"] = round(water95(Psat=psat, X=x, desc="u"), 8)
                        ans["Cp"] = round(water95(Psat=psat, X=x, desc="Cp"), 8)
                        ans["Cv"] = round(water95(Psat=psat, X=x, desc="Cv"), 8)
                        units[0] = "MPa"
                        units[1] = self.unit1.get()

        if x == 0:
            ans["Fase"] = "Cair"
        elif x == 1:
            ans["Fase"] = "Uap"
        elif (x > 0) and (x < 1):
            ans["Fase"] = "Campuran"

        self.props["saturation"].append(ans)

        self.func_output(variables=ans, units=units, mainframe=self.frame02, idx="frame02")

    def fun_cls1(self, event=None):
        if self.menu0.get() == "P":
            self.input1.set("")
            self.cbb2.current(1)
            self.cbb3.current(0)
        elif self.menu0.get() == "T":
            self.input1.set("")
            self.cbb2.current(1)
            self.cbb3.current(0)

        self.input2.set("")

        for col in self.cols["frame02"]:
            col.grid_forget()

        self.cols["frame02"] = list()

    def func_output(self, mainframe, idx, variables=dict(), units=list()):
        i = 4
        for var, val in variables.items():
            # column 0
            col1 = ttk.Label(mainframe, text=var, width=14, font=font.Font(size=10))
            col1.grid(column=0, row=i, padx=(0, 10), sticky=tk.W)

            #column 1
            col2 = ttk.Label(mainframe, text=val, width=16, font=font.Font(size=10))
            col2.grid(column=1, row=i, padx=(0, 5), sticky=tk.W)
            self.cols[idx].append(col1)
            self.cols[idx].append(col2)
            i += 1

        #column 2
        k = 4
        for unit in units:
            col3 = ttk.Label(mainframe, text=unit, width=7, font=font.Font(size=10))
            col3.grid(column=2, row=k, sticky=tk.W)
            self.cols[idx].append(col3)
            k += 1

    def func_tab1(self):
        lbl1 = ttk.Label(self.frame10, text="SATU FASE", justify="center", font=font.Font(size=16))
        lbl2 = ttk.Label(self.frame10, text="P", justify="left", font=font.Font(size=10))
        lbl3 = ttk.Label(self.frame10, text="T", justify="left", font=font.Font(size=10))
        entri1 = ttk.Entry(self.frame10, width=18, textvariable=self.input3, font=font.Font(size=10))
        entri2 = ttk.Entry(self.frame10, width=18, textvariable=self.input4, font=font.Font(size=10))
        cbb1 = ttk.Combobox(self.frame10, values=("Pa", "KPa", "MPa"), width=4, textvariable=self.unit3,
                            state="readonly", font=font.Font(size=10))
        cbb2 = ttk.Combobox(self.frame10, values=("C", "K"), width=4, textvariable=self.unit4, state="readonly",
                            font=font.Font(size=10))
        btn2 = ttk.Button(self.frame11, text="Hitung", command=self.func_btn2)
        cls2 = ttk.Button(self.frame11, text="Reset", command=self.func_cls2)

        cbb1.current(1)
        cbb2.current(1)

        lbl1.grid(row=0, column=1, pady=(0, 20), sticky="nw")
        lbl2.grid(row=1, column=0, padx=(0, 30), pady=(0, 20), sticky="nw")
        lbl3.grid(row=2, column=0, padx=(0, 30), sticky="nw")
        entri1.grid(row=1, column=1, padx=(0, 10), pady=(0, 20), sticky="nw")
        entri2.grid(row=2, column=1, padx=(0, 10), sticky="nw")
        cbb1.grid(row=1, column=2, pady=(0, 20), sticky="nw")
        cbb2.grid(row=2, column=2, sticky="nw")
        btn2.grid(column=0, row=3, padx=(20, 100), sticky="nw")
        cls2.grid(column=2, row=3, padx=(0, 20), sticky="nw")

    def func_btn2(self, event=None):
        ans = dict()
        t = tsat = math.nan
        outs = ["Tekanan",
                "Suhu",
                "Massa jenis",
                "Volume jenis",
                "Entropi",
                "Entalpi",
                "Energi dalam",
                "Cp",
                "Cv"]
        units = ["KPa", "K", "Kg/m³", "m³/Kg", "KJ/Kg", "KJ/Kg", "KJ/Kg", "KJ/Kg*K", "KJ/Kg*K"]

        for idx in outs:
            ans[idx] = math.nan

        if (self.input3.get() != "") and (self.input4.get() != ""):
            ans["Tekanan"] = float(self.input3.get())
            ans["Suhu"] = float(self.input4.get())
            p = self.press_converter(value=self.input3, unit=self.unit3)
            t = self.temp_converter(value=self.input4, unit=self.unit4)

            if (not math.isnan(p)) and (not math.isnan(t)):
                tsat = water95(P=p, T=t, desc="Tsat")
                ans["Massa jenis"] = round(water95(P=p, T=t, desc="rho"), 8)
                ans["Volume jenis"] = round(water95(P=p, T=t, desc="v"), 8)
                ans["Entropi"] = round(water95(P=p, T=t, desc="s"), 8)
                ans["Entalpi"] = round(water95(P=p, T=t, desc="h"), 8)
                ans["Energi dalam"] = round(water95(P=p, T=t, desc="u"), 8)
                ans["Cp"] = round(water95(P=p, T=t, desc="Cp"), 8)
                ans["Cv"] = round(water95(P=p, T=t, desc="Cv"), 8)

        if t < tsat:
            ans["Fase"] = "Cair"
        elif (t > tsat) and (t < TEMPC):
            ans["Fase"] = "Uap"
        elif t >= TEMPC:
            ans["Fase"] = "Super Uap"

        units[0] = self.unit3.get()
        units[1] = self.unit4.get()

        self.props["singlephase"].append(ans)

        self.func_output(variables=ans, units=units, mainframe=self.frame12, idx="frame12")

    def func_cls2(self, event=None):
        self.input3.set("")
        self.input4.set("")

        for col in self.cols["frame12"]:
            col.grid_forget()

        self.cols["frame12"] = list()


_ui_ = WaterPropUi()