def _convert(list_convert):
    """
    Конвертирует список с p[(5,), (8,), ...] к [5, 8, ...].

    Parameters
    ----------
    list_convert : TYPE
        DESCRIPTION.

    Returns
    -------
    list
        DESCRIPTION.

    """
    return [item[0] for item in list_convert]


def total_cost(list_quantity, list_price):
    """
    Считает общую сумму заказа и козвращает результат.

    Parameters
    ----------
    list_quantity : TYPE
        DESCRIPTION.
    list_price : TYPE
        DESCRIPTION.

    Returns
    -------
    order_total_cost : int
        DESCRIPTION.

    """
    order_total_cost = 0
    for idx, item in enumerate(list_price):
        order_total_cost += list_quantity[idx] * list_price[idx]

    return round(order_total_cost, 2)


def get_total_cost(BD):
    """
    Возвращает общую стоимость товара.

    Parameters
    ----------
    BD : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    # получаем список, все product_id заказа
    all_product_id = BD.select_all_product_id()
    # получаем список стоимость по всем позициям заказа в виде обычного списка
    all_price = [BD.select_single_product_price(item) for item in all_product_id]
    # получаем список количества по всем позициям заказа в виде обычного списка
    all_quantity = [BD.select_order_quantity(item) for item in all_product_id]
    # возвращает общую стоимость товара
    return total_cost(all_quantity, all_price)


def total_quantity(list_quantity):
    """
    Считает общее количество заказанной еденицы товара и возвращает результат.

    Parameters
    ----------
    list_quantity : TYPE
        DESCRIPTION.

    Returns
    -------
    order_total_quantity : TYPE
        DESCRIPTION.

    """
    order_total_quantity = 0

    for item in list_quantity:
        order_total_quantity += item

    return order_total_quantity


def get_total_quantity(BD):
    """
    Возврашает общее количество заказанной еденицы товара.

    Parameters
    ----------
    BD : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    # получаем список, все product_id заказа
    all_product_id = BD.select_all_product_id()
    # получаем список количества по всем позициям заказа в виде обычного списка
    all_quantity = [BD.select_order_quantity(item) for item in all_product_id]
    # возврашаем количество товарных позиций
    return total_quantity(all_quantity)
