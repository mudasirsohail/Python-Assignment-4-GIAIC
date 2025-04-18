def main():
    qasim: int = 21  # qasim's age is given
    ahmed: int = qasim + 6  # ahmed is 6 years older than qasim
    mussawir: int = ahmed + 20  # mussawir is 20 years older than ahmed
    mudasir: int = mussawir + qasim  # mudasir is mussawir's age + qasim's age
    naaz: int = mussawir  # naaz is the same age as mussawir

    # Print out all of the ages exactly as required
    print("qasim is " + str(qasim))
    print("ahmed is " + str(ahmed))
    print("mussawir is " + str(mussawir))
    print("mudasir is " + str(mudasir))
    print("naaz is " + str(naaz))

# Required line to call the main() function
if __name__ == '__main__':
    main()
