import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
  
    window = turtle.Screen()
    window.bgcolor("teal")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)  
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)  

    window.mainloop()
   


    
def main():
    user_input =input("Please, specify the level of recursion >>>>>")
        
    if user_input.isdigit():
        draw_koch_snowflake(int(user_input))
    else:
        print('Invalid level. Enter the integer, please')
        main()


if __name__ == '__main__':
    main()
