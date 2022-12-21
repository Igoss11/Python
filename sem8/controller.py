import view
import model
import logger


def run_calc():
    mode = view.choose()
    if mode == '1':
        expr = view.get_expr()
        result = model.execute_expr(expr)
        view.show_res(result)
        logger.log_exec(expr, result)
    elif mode == '2':
        expr = view.get_expr()
        result = model.solve_eq(expr)
        view.show_res(result)
        logger.log_exec(expr, result)
    elif mode == '3':
        expr = view.get_expr()
        result = model.simpify_pol(expr)
        view.show_res(result)
        logger.log_exec(expr, result)
    elif mode == '4':
        history = logger.get_history()
        view.show_history(history)
    else:
        view.error_mode()
