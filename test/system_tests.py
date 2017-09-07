from iota import *
from logging import basicConfig, DEBUG, getLogger
from sys import stderr
import time
from bot_api import api, Database
import sqlite3
import unittest
import config

#basicConfig(level=DEBUG, stream=stderr, format='%(levelname)s: %(asctime)s: %(message)s')
#logger = getLogger(__name__)
#logger.setLevel(DEBUG)

test_seed = b'A'*81

class SystemTests(unittest.TestCase):

        """
        Test Transactions
        Send 100 transfers and verify that each one is properly received
        """
        def test_systems(self):
            bot_api_send = api(b'LMFWBJLBIGZZXYSHXIO9PAUVQZ9AYQBRT9ERSUQEDRAGMILTQKXOSVYJFNOMRSFYGRMFFMLF9CUA9FNZS')
            bot_api_receive = api(b'PYBTQIJYAYYSO9LLXCWKC9QDIJNWUGJWBGTUNVMFVRTCNWYZRRDEZCMPYCLOYCBGHUIITKPDR9YRCJHKY')
            bot_db_send = Database('test_db1_send.db')
            bot_db_receive = Database('test_db_receive.db')
            for i in range(1,100):
                starting_balance = bot_api_receive.get_account_balance(bot_db_receive.get_address_index())
                print('Starting Balance: {0}'.format(starting_balance))
                #Get the receiving address
                while True:
                    address_index = bot_db_receive.get_address_index()
                    address = bot_api_receive.get_new_address(address_index)
                    bot_db_receive.add_used_address(address_index,address._trytes.decode("utf-8"))
                    if bot_api_receive.get_balance(address) == 0:
                        break
                #Get the new sending address
                address_index = bot_db_send.get_address_index()
                new_address = bot_api_send.get_new_address(address_index)
                bot_db_send.add_used_address(address_index,address._trytes.decode("utf-8"))

                transaction = bot_api_send.send_transfer(address,i,new_address,address_index)
                print('{0} sent to address.'.format(i))
                print(transaction['bundle'].hash)
                print(transaction['bundle'].tail_transaction.hash)
                confirmed = False
                start_time = time.time()
                while not confirmed:
                    confirmed = bot_api_send.check_transaction(transaction)
                    if (time.time() - start_time) > (60) and not confirmed:
                        print('Replaying Bundle')
                        #confirmed = True
                        bot_api_send.replay_bundle(transaction)
                print('Transaction Confirmed')
                self.assertEqual(bot_api_receive.get_account_balance(),starting_balance+i)

unittest.main()
