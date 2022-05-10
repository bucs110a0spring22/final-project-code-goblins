import pygame
from src import controller





def main():
    control = controller.Controller()
    control.mainloop()

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######


# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

# Final class diagram has not been completed;
# Responsibility of back end