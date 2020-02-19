import contextlib

class Connection:
    def __init__(self):
        self.xid = 0

    def _start_transaction(self):
        print('starting transaction', self.xid)
        rslt = self.xid
        self.xid = self.xid + 1
        return rslt

    def _commit_transaction(self, xid):
        print('committing transaction', xid)
    
    def _rollback_transaction(self, xid):
        print('rolling back transaction', xid)


class Transaction:
    def __init__(self, conn):
        self.conn = conn
        self.xid = conn._start_transaction()

    def commit(self):
        self.conn._commit_transaction(self.xid)
    
    def rollback(self):
        self.conn._rollback_transaction(self.xid)


@contextlib.contextmanager
def start_transaction(connection):
    tx = Transaction(connection)
    try:
        yield tx
    except:
        tx.rollback()
        raise
    tx.commit()             # commits transaction if with block exits normally


if __name__ == "__main__":
    ''' Use them without context managers '''
    # conn = Connection()
    # xact = Transaction(conn)        # starting transaction 0
    # xact.commit()                   # committing transaction 0


    ''' Using the context manager with exception '''
    conn = Connection()
    try:
        with start_transaction(conn) as tx:
            x = 1 + 1
            raise ValueError()
            y = x + 2
            print('transaction 0 =', x, y)
    except ValueError:
        print('Transaction failed')
    # starting transaction 0
    # rolling back transaction 0
    # Transaction failed

    ''' Using the context manager without the  exception '''
    try:
        with start_transaction(conn) as tx:
            x = 1 + 1
            y = x + 2
            print('transaction 1 =', x, y)
    except ValueError:
        assert False
    # starting transaction 1
    # transaction 1 = 2 4
    # committing transaction 1
