def outer(logo):
    def inner(msg):
        print(f"{msg}+{logo}")
    return inner

fn1 = outer("floyd")
fn1("123")