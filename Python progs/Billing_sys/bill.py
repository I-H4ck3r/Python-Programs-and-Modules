from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
        def __init__(self,root):
                self.root = root
                self.root.geometry("1920x1080+0+0")
                self.root.title("BILLING SOFTWARE")
                bg_color = "#074463"
                title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("Times New Roman",30,"bold"),pady=2)
                title.pack(fill=X)

                ############################ VARIABLES ########################
                ######## Cosmetics ###########
                self.soap=IntVar()
                self.face_cream=IntVar()
                self.face_wash=IntVar()
                self.hair_spray=IntVar()
                self.hair_gel=IntVar()
                self.body_lotion=IntVar()
                
                ######### Grocery #######
                self.rice=IntVar()
                self.food_oil=IntVar()
                self.dal=IntVar()
                self.wheat_flour=IntVar()
                self.sugar=IntVar()
                self.tea=IntVar()

                ###### Cold drink #########   
                self.fanta=IntVar()
                self.coca_cola=IntVar()
                self.thumbs_up=IntVar()
                self.sprite=IntVar()
                self.mountain_dew=IntVar()
                self.limca=IntVar()

                ######### Total Product Price & Tax Variable #############
                self.cosmetic_price=StringVar()
                self.grocery_price=StringVar()
                self.cold_drink_price=StringVar()
                self.cosmetic_tax=StringVar()
                self.grocery_tax=StringVar()
                self.cold_drink_tax=StringVar()

                ######### Customer #######
                self.c_name=StringVar()
                self.c_phn=StringVar()

                self.bill_no=StringVar()
                x = random.randint(1000,9999)
                self.bill_no.set(str(x))
                
                self.search_bill=StringVar()


                ############################## CUSTOMER DETAIL FRAME ##############################

                F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,bg=bg_color,fg="gold",font=("Times New Roman",15,"bold"),pady=2)
                F1.place(x=0,y=70,relwidth=1)

                cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("Times New Roman",15,"bold"),pady=2)
                cname_lbl.grid(row=0,column=0,padx=20,pady=5)
                cname_txt=Entry(F1,width=16,textvariable=self.c_name,font="Arial 15",bd=7,relief=SUNKEN)
                cname_txt.grid(row=0,column=1,padx=10,pady=5)

                cphn_lbl=Label(F1,text="Phone no.",bg=bg_color,fg="white",font=("Times New Roman",15,"bold"),pady=2)
                cphn_lbl.grid(row=0,column=2,padx=20,pady=5)
                cphn_txt=Entry(F1,width=16,textvariable=self.c_phn,font="Arial 15",bd=7,relief=SUNKEN)
                cphn_txt.grid(row=0,column=3,padx=10,pady=5)

                c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("Times New Roman",15,"bold"),pady=2)
                c_bill_lbl.grid(row=0,column=4,padx=20,pady=5)
                c_bill_txt=Entry(F1,width=16,textvariable=self.search_bill,font="Arial 15",bd=7,relief=SUNKEN)
                c_bill_txt.grid(row=0,column=5,padx=10,pady=5)

                bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="Arial 12 bold")
                bill_btn.grid(row=0,column=6,padx=60,pady=5)

                ################################# COSMETICS FRAME ####################################

                F2=LabelFrame(self.root,text="Cosmetics",bd=10,relief=GROOVE,bg=bg_color,fg="gold",font=("Times New Roman",15,"bold"),pady=2)
                F2.place(x=0,y=160,height=475,width=380)

                bath_lbl=Label(F2,text="Bathing Soap",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                bath_lbl.grid(row=0,column=0,padx=10,pady=10,sticky='w')
                bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                bath_txt.grid(row=0,column=1,padx=10,pady=10)

                face_cream_lbl=Label(F2,text="Face Cream",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                face_cream_lbl.grid(row=1,column=0,padx=10,pady=10,sticky='w')
                face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                face_cream_txt.grid(row=1,column=1,padx=10,pady=10)

                face_wash_lbl=Label(F2,text="Face Wash",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                face_wash_lbl.grid(row=2,column=0,padx=10,pady=10,sticky='w')
                face_wash_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                face_wash_txt.grid(row=2,column=1,padx=10,pady=10)

                hair_spray_lbl=Label(F2,text="Hair Spray",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                hair_spray_lbl.grid(row=3,column=0,padx=10,pady=10,sticky='w')
                hair_spray_txt=Entry(F2,width=10,textvariable=self.hair_spray,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                hair_spray_txt.grid(row=3,column=1,padx=10,pady=10)

                hair_gel_lbl=Label(F2,text="Hair Gel",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                hair_gel_lbl.grid(row=4,column=0,padx=10,pady=10,sticky='w')
                hair_gel_txt=Entry(F2,width=10,textvariable=self.hair_gel,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                hair_gel_txt.grid(row=4,column=1,padx=10,pady=10)

                body_lotion_lbl=Label(F2,text="Body Lotion",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                body_lotion_lbl.grid(row=5,column=0,padx=10,pady=10,sticky='w')
                body_lotion_txt=Entry(F2,width=10,textvariable=self.body_lotion,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                body_lotion_txt.grid(row=5,column=1,padx=10,pady=10)

        ################################# GROCERY FRAME ####################################

                F3=LabelFrame(self.root,text="Grocery",bd=10,relief=GROOVE,bg=bg_color,fg="gold",font=("Times New Roman",15,"bold"),pady=2)
                F3.place(x=380,y=160,height=475,width=380)

                g1_lbl=Label(F3,text="Rice",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                g1_lbl.grid(row=0,column=0,padx=10,pady=10,sticky='w')
                g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                g1_txt.grid(row=0,column=1,padx=10,pady=10)

                g2_lbl=Label(F3,text="Food Oil",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                g2_lbl.grid(row=1,column=0,padx=10,pady=10,sticky='w')
                g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                g2_txt.grid(row=1,column=1,padx=10,pady=10)

                g3_lbl=Label(F3,text="Daal",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                g3_lbl.grid(row=2,column=0,padx=10,pady=10,sticky='w')
                g3_txt=Entry(F3,width=10,textvariable=self.dal,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                g3_txt.grid(row=2,column=1,padx=10,pady=10)

                g4_lbl=Label(F3,text="Wheat Flour",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                g4_lbl.grid(row=3,column=0,padx=10,pady=10,sticky='w')
                g4_txt=Entry(F3,width=10,textvariable=self.wheat_flour,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                g4_txt.grid(row=3,column=1,padx=10,pady=10)

                g5_lbl=Label(F3,text="Sugar",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                g5_lbl.grid(row=4,column=0,padx=10,pady=10,sticky='w')
                g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                g5_txt.grid(row=4,column=1,padx=10,pady=10)

                g6_lbl=Label(F3,text="Tea",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                g6_lbl.grid(row=5,column=0,padx=10,pady=10,sticky='w')
                g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                g6_txt.grid(row=5,column=1,padx=10,pady=10)

        ################################# COLD DRINKS FRAME ####################################

                F4=LabelFrame(self.root,text="Cold Drinks",bd=10,relief=GROOVE,bg=bg_color,fg="gold",font=("Times New Roman",15,"bold"),pady=2)
                F4.place(x=760,y=160,height=475,width=380)

                c1_lbl=Label(F4,text="Fanta",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                c1_lbl.grid(row=0,column=0,padx=10,pady=10,sticky='w')
                c1_txt=Entry(F4,width=10,textvariable=self.fanta,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                c1_txt.grid(row=0,column=1,padx=10,pady=10)

                c2_lbl=Label(F4,text="Coca Cola",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                c2_lbl.grid(row=1,column=0,padx=10,pady=10,sticky='w')
                c2_txt=Entry(F4,width=10,textvariable=self.coca_cola,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                c2_txt.grid(row=1,column=1,padx=10,pady=10)

                c3_lbl=Label(F4,text="Thumbs up",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                c3_lbl.grid(row=2,column=0,padx=10,pady=10,sticky='w')
                c3_txt=Entry(F4,width=10,textvariable=self.thumbs_up,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                c3_txt.grid(row=2,column=1,padx=10,pady=10)

                c4_lbl=Label(F4,text="Sprite",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                c4_lbl.grid(row=3,column=0,padx=10,pady=10,sticky='w')
                c4_txt=Entry(F4,width=10,textvariable=self.sprite,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                c4_txt.grid(row=3,column=1,padx=10,pady=10)

                c5_lbl=Label(F4,text="Mountain Dew",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                c5_lbl.grid(row=4,column=0,padx=10,pady=10,sticky='w')
                c5_txt=Entry(F4,width=10,textvariable=self.mountain_dew,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                c5_txt.grid(row=4,column=1,padx=10,pady=10)

                c6_lbl=Label(F4,text="Limca",bg=bg_color,fg="lightgreen",font=("Times New Roman",16,"bold"),pady=2)
                c6_lbl.grid(row=5,column=0,padx=10,pady=10,sticky='w')
                c6_txt=Entry(F4,width=10,textvariable=self.limca,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN)
                c6_txt.grid(row=5,column=1,padx=10,pady=10)

                ############################# BILL AREA ####################################
                F5=LabelFrame(self.root,bd=10,relief=GROOVE)
                F5.place(x=1140,y=160,height=460,width=385)
                bill_title=Label(F5,text="Bill Area",font="Arial 15 bold",bd=7,relief=GROOVE)
                bill_title.pack(fill=X)

                scroll_y=Scrollbar(F5,orient=VERTICAL)
                self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_y.config(command=self.txtarea.yview)
                self.txtarea.pack(fill=BOTH,expand=1)

                ############################ BUTTON FRAME #################################
                F6=LabelFrame(self.root ,text="Bill Menu",bd=10,relief=GROOVE,bg=bg_color,fg="gold",font=("Times New Roman",15,"bold"),pady=2)
                F6.place(x=0,y=620,height=195,relwidth=2)

                m1_lbl=Label(F6,text="Total Cosmetic Price",font=("Times New Roman",14,"bold"),bg=bg_color,fg="white")
                m1_lbl.grid(row=0,column=0,padx=20,pady=3,sticky='w')
                m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="Arial 10 bold",bd=7,relief=SUNKEN)
                m1_txt.grid(row=0,column=1,padx=10,pady=3)

                m2_lbl=Label(F6,text="Total Grocery Price",font=("Times New Roman",14,"bold"),bg=bg_color,fg="white")
                m2_lbl.grid(row=1,column=0,padx=20,pady=3,sticky='w')
                m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="Arial 10 bold",bd=7,relief=SUNKEN)
                m2_txt.grid(row=1,column=1,padx=10,pady=3)

                m3_lbl=Label(F6,text="Total Cold Drink Price",font=("Times New Roman",14,"bold"),bg=bg_color,fg="white")
                m3_lbl.grid(row=2,column=0,padx=20,pady=3,sticky='w')
                m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="Arial 10 bold",bd=7,relief=SUNKEN)
                m3_txt.grid(row=2,column=1,padx=10,pady=3)

                c1_lbl=Label(F6,text="Cosmetic Tax",font=("Times New Roman",14,"bold"),bg=bg_color,fg="white")
                c1_lbl.grid(row=0,column=3,padx=20,pady=3,sticky='w')
                c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="Arial 10 bold",bd=7,relief=SUNKEN)
                c1_txt.grid(row=0,column=4,padx=10,pady=3)

                c2_lbl=Label(F6,text="Grocery Tax",font=("Times New Roman",14,"bold"),bg=bg_color,fg="white")
                c2_lbl.grid(row=1,column=3,padx=20,pady=3,sticky='w')
                c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="Arial 10 bold",bd=7,relief=SUNKEN)
                c2_txt.grid(row=1,column=4,padx=10,pady=3)

                c3_lbl=Label(F6,text="Cold Drink Tax",font=("Times New Roman",14,"bold"),bg=bg_color,fg="white")
                c3_lbl.grid(row=2,column=3,padx=20,pady=3,sticky='w')
                c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font="Arial 10 bold",bd=7,relief=SUNKEN)
                c3_txt.grid(row=2,column=4,padx=10,pady=3)

                btn_f=Frame(F6,bd=7,relief=GROOVE)
                btn_f.place(x=850,width=585,height=105)

                total_btn=Button(btn_f,text="Total",command=self.total,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="Arial 14 bold")
                total_btn.grid(row=0,column=0,padx=5,pady=8)

                gbill_btn=Button(btn_f,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="Arial 14 bold")
                gbill_btn.grid(row=0,column=1,padx=5,pady=8)

                clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="Arial 14 bold")
                clear_btn.grid(row=0,column=2,padx=5,pady=8)

                exit_btn=Button(btn_f,text="Exit",command=self.exit_app,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="Arial 14 bold")
                exit_btn.grid(row=0,column=3,padx=5,pady=8)
                self.welcome_bill()


        def total(self):
                self.c_s_p=self.soap.get()*50
                self.c_fc_p=self.face_cream.get()*120
                self.c_fw_p=self.face_wash.get()*90
                self.c_hs_p=self.hair_spray.get()*200
                self.c_hg_p=self.hair_gel.get()*180
                self.c_bl_p=self.body_lotion.get()*340
                self.total_cosmetic_price=float(
                                                self.c_s_p+
                                                self.c_fc_p+
                                                self.c_fw_p+
                                                self.c_hs_p+
                                                self.c_hg_p+
                                                self.c_bl_p
                                                )
                self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
                self.c_tax=round((self.total_cosmetic_price*0.05),2)
                self.cosmetic_tax.set("Rs. "+str(self.c_tax))


                self.g_r_p=self.rice.get()*80
                self.g_fo_p=self.food_oil.get()*180
                self.g_d_p=self.dal.get()*70
                self.g_wf_p=self.wheat_flour.get()*240
                self.g_s_p=self.sugar.get()*60
                self.g_t_p=self.tea.get()*150
                self.total_grocery_price=float(
                                                self.g_r_p+
                                                self.g_fo_p+
                                                self.g_d_p+
                                                self.g_wf_p+
                                                self.g_s_p+
                                                self.g_t_p
                                                )
                self.grocery_price.set("Rs. "+str(self.total_grocery_price))
                self.g_tax=round((self.total_grocery_price*0.1),2)
                self.grocery_tax.set("Rs. "+str(self.g_tax))


                self.d_f_p=self.fanta.get()*60
                self.d_c_p=self.coca_cola.get()*70
                self.d_t_p=self.thumbs_up.get()*60
                self.d_s_p=self.sprite.get()*70
                self.d_md_p=self.mountain_dew.get()*80
                self.d_l_p=self.limca.get()*50
                self.total_cold_drink_price=float(
                                                self.d_f_p+
                                                self.d_c_p+
                                                self.d_t_p+
                                                self.d_s_p+
                                                self.d_md_p+
                                                self.d_l_p
                                                )
                self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
                self.d_tax=round((self.total_cold_drink_price*0.05),2)
                self.cold_drink_tax.set("Rs. "+str(self.d_tax))

                self.total_price=float(self.total_cosmetic_price + self.total_grocery_price + self.total_cold_drink_price)
                self.total_tax=float(self.c_tax + self.g_tax + self.d_tax)
                self.total_bill=float(self.total_price + self.total_tax)

        def welcome_bill(self):
                self.txtarea.delete('1.0', END)
                self.txtarea.insert(END,"\tWelcome Div Retail")
                self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
                self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
                self.txtarea.insert(END,f"\n Phone Number : {self.c_phn.get()}")
                self.txtarea.insert(END,f"\n=======================================")
                self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
                self.txtarea.insert(END,f"\n=======================================")
                self.txtarea.insert(END,f"\n=======================================")

        def bill_area(self):
                if self.c_name.get()=="" or self.c_phn.get()=="":
                        messagebox.showerror("Error","Customer Details are must")
                elif self.cosmetic_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0"  and self.cold_drink_price.get() == "Rs. 0.0":
                        messagebox.showerror("Error","No Product purchased")
                else:
                        self.welcome_bill()
                        ######## COSMETICS ##########
                        if self.soap.get()!=0:
                                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
                        if self.face_cream.get()!=0:
                                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
                        if self.face_wash.get()!=0:
                                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
                        if self.hair_spray.get()!=0:
                                self.txtarea.insert(END,f"\n Hair Spray\t\t{self.hair_spray.get()}\t\t{self.c_hs_p}")
                        if self.hair_gel.get()!=0:
                                self.txtarea.insert(END,f"\n Hair Gel\t\t{self.hair_gel.get()}\t\t{self.c_hg_p}")
                        if self.body_lotion.get()!=0:
                                self.txtarea.insert(END,f"\n Body Lotion\t\t{self.body_lotion.get()}\t\t{self.c_bl_p}")
                        
                        ######## GROCERY ##########
                        if self.rice.get()!=0:
                                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.g_r_p}")
                        if self.food_oil.get()!=0:
                                self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")
                        if self.dal.get()!=0:
                                self.txtarea.insert(END,f"\n Daal\t\t{self.dal.get()}\t\t{self.g_d_p}")
                        if self.wheat_flour.get()!=0:
                                self.txtarea.insert(END,f"\n Wheat Flour\t\t{self.wheat_flour.get()}\t\t{self.g_wf_p}")
                        if self.sugar.get()!=0:
                                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
                        if self.tea.get()!=0:
                                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")
                        
                        ######## COLD DRINKS ##########
                        if self.fanta.get()!=0:
                                self.txtarea.insert(END,f"\n Fanta\t\t{self.fanta.get()}\t\t{self.d_f_p}")
                        if self.coca_cola.get()!=0:
                                self.txtarea.insert(END,f"\n Coca Cola\t\t{self.coca_cola.get()}\t\t{self.d_c_p}")
                        if self.thumbs_up.get()!=0:
                                self.txtarea.insert(END,f"\n Thumbs Up\t\t{self.thumbs_up.get()}\t\t{self.d_t_p}")
                        if self.sprite.get()!=0:
                                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")
                        if self.mountain_dew.get()!=0:
                                self.txtarea.insert(END,f"\n Mountain Dew\t\t{self.mountain_dew.get()}\t\t{self.d_md_p}")
                        if self.limca.get()!=0:
                                self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")
                        
                        self.txtarea.insert(END,f"\n---------------------------------------")
                        if self.cosmetic_tax.get()!="Rs. 0.0":
                                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
                        if self.grocery_tax.get()!="Rs. 0.0":
                                self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
                        if self.cold_drink_tax.get()!="Rs. 0.0":
                                self.txtarea.insert(END,f"\n Cold Drink Tax\t\t\t{self.cold_drink_tax.get()}")
                        self.txtarea.insert(END,f"\n---------------------------------------")

                        self.txtarea.insert(END,f"\n---------------------------------------")
                        self.txtarea.insert(END,f"\n Total Price\t\t\t{self.total_price}")
                        self.txtarea.insert(END,f"\n Total Tax\t\t\t{self.total_tax}")
                        self.txtarea.insert(END,f"\n Total Bill\t\t\t{self.total_bill}")
                        self.txtarea.insert(END,f"\n---------------------------------------")
                        self.save_bill()

        def save_bill(self):
                op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
                if op>0:
                        self.bill_data=self.txtarea.get('1.0',END)
                        f1=open("bills/"+str(self.bill_no.get())+".txt","w")
                        f1.write(self.bill_data)
                        f1.close()
                        messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} saved successfully")
                else:
                        return
        
        def find_bill(self):
                present="no"
                for i in os.listdir("bills/"):
                        if i.split('.')[0]==self.search_bill.get():
                                f1=open(f"bills/{i}","r")
                                self.txtarea.delete('1.0',END)
                                for d in f1:
                                        self.txtarea.insert(END,d)
                                f1.close()
                                present="yes"
                if present=="no":
                        messagebox.showerror("Error","Invalid Bill no.")
        def clear_data(self):
                op=messagebox.askyesno("CLEAR","Do you really want to clear data?")
                if (op>0):
                        ######## Cosmetics ###########
                        self.soap.set(0)
                        self.face_cream.set(0)
                        self.face_wash.set(0)
                        self.hair_spray.set(0)
                        self.hair_gel.set(0)
                        self.body_lotion.set(0)
                        
                        ######### Grocery #######
                        self.rice.set(0)
                        self.food_oil.set(0)
                        self.dal.set(0)
                        self.wheat_flour.set(0)
                        self.sugar.set(0)
                        self.tea.set(0)

                        ###### Cold drink #########   
                        self.fanta.set(0)
                        self.coca_cola.set(0)
                        self.thumbs_up.set(0)
                        self.sprite.set(0)
                        self.mountain_dew.set(0)
                        self.limca.set(0)

                        ######### Total Product Price & Tax Variable #############
                        self.cosmetic_price.set("")
                        self.grocery_price.set("")
                        self.cold_drink_price.set("")
                        self.cosmetic_tax.set("")
                        self.grocery_tax.set("")
                        self.cold_drink_tax.set("")

                        ######### Customer #######
                        self.c_name.set("")
                        self.c_phn.set("")
                        self.bill_no.set("")
                        x = random.randint(1000,9999)
                        self.bill_no.set(str(x))
                        
                        self.search_bill.set("")
                        self.welcome_bill()
        def exit_app(self):
                op=messagebox.askyesno("EXIT","Do you really want to exit?")
                if op>0:
                        self.root.destroy()                     

root = Tk()
obj = Bill_App(root)
root.mainloop()