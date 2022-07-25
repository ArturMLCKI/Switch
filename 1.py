day_of_the_week = 'Monday'

match day_of_the_week:
    case 'Monday':
        print("Początki są zawsze najgorsze")
    case 'Wednesday':
        print("Środa to taka mała sobota")
    case 'Friday':
        print("Zaczyna się weekend")
    case 'Sunday':
        print("Już jutro do pracy HURRRA!")
    case _:
        print("Dzień jak co dzień")