def formatDate(date):
    import dateutil.parser

    try:
        dateFormatted = dateutil.parser.parse(date)
    except ValueError:
        raise ValueError(
            "Purchase date is outside of boundaries. (req. '2015-1-1')")
    except TypeError:
        raise TypeError(
            "Purchase date has wrong data type. (req. '2015-1-1') ")
    except:
        print("Purchase date: unknown error.")
    return dateFormatted
