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

class BotUnitTests(unittest.TestCase):

        #----------------TEST REGEX FUNCTIONS -----------------#
        
        """
        Test is_deposit_request
        Sunny Day 1
        Preconditions:
           Message subject contains 'deposit' 
           Message body does not contain 'deposit'
        Postconditions:
           Function returns True
        """
        def test_is_deposit_requests_sunny_1(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'asdkfjsaddepositsadlkfjlasd'
                body = 'asdjalksjdsa'
            self.assertTrue(bot_api.is_deposit_request(Message))
        
        """
        Test is_deposit_request
        Sunny Day 2
        Preconditions:
           Message subject does not contain 'deposit'
           Message body contains 'deposit'
        Postconditions:
            Function returns True
        """
        def test_is_deposit_request_sunny_2(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'asjdkhasjkd'
                body = 'asdfkjasddepositklsafdj;lsdjf'
            self.assertTrue(bot_api.is_deposit_request(Message))

        """
        Test is_deposit_request
        Sunny Day 3
        Preconditions:
            Message subject contains 'deposit'
            Message body contains 'deposit'
        Postconditions:
            Function returns True
        """
        def test_is_deposit_request_sunny_3(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'askdljasdepositasdfkljsad'
                body = 'aksljhfddepositaslkdj'
            self.assertTrue(bot_api.is_deposit_request(Message))

        """
        Test is_deposit_request
        Rainy Day 1
        Preconditions:
            Message subject does not contain 'deposit'
            Message body does not contain 'deposit'
        Postconditions:
            Function returns False
        """
        def test_is_deposit_request_rainy_1(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'askldjflkasd'
                body = 'askljfslad'
            self.assertFalse(bot_api.is_deposit_request(Message))
            
        """
        Test is_withdraw_request
        Sunny Day 1
        Preconditions:
            Message subject contains 'withdraw'
            Message subject does not contain 'withdraw'
        Postconditions:
            Function returns True
        """
        def test_is_withdraw_request_sunny_1(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'askdljaswithdraw'
                body = 'asjkhnfsda'
            self.assertTrue(bot_api.is_withdraw_request(Message))
    
        """
        Test is_withdraw_requests
        Sunny Day 2
        Preconditions:
            Message subject does not contain 'withdraw'
            Message body contains 'withdraw'
        Postconditions:
            Function returns True
        """
        def test_is_withdraw_request_sunny_2(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'asjkdhas'
                body = 'asdklfjasdwithdrawasdfkjas'
            self.assertTrue(bot_api.is_withdraw_request(Message))
            
        """
        Test is_withdraw_request
        Sunny Day 3
        Preconditions:
            Message subject contains 'withdraw'
            Message body contains 'withdraw'
        Postconditions:
            Function returns True
        """
        def test_is_withdraw_request_sunny_3(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'sakljlaskdwithdrawfkljaslkdf'
                body = 'askjldhaswithdrawkladjskld'
            self.assertTrue(bot_api.is_withdraw_request(Message))

        """
        Test is_withdraw_request
        Rainy Day 1
        Preconditions:
            Message subject does not contain 'withdraw'
            Message body does not contain 'withdraw'
        Postconditions:
            Function returns False
        """
        def test_is_withdraw_request_sunny_3(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'asdklfjlaksd'
                body = 'askljfasdf'
            self.assertFalse(bot_api.is_withdraw_request(Message))
    
        """
        Test is_balance_request
        Sunny Day 1
        Preconditions:
            Message subject contains 'balance'
            Message body does not contain 'balance'
        Postconditions:
            Function returns True
        """
        def test_is_balance_request_sunny_1(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'asklfjaskldbalanceasdkfljasd'
                body = 'sakjalhfklas'
            self.assertTrue(bot_api.is_balance_request(Message))
        
        """
        Test is_balance_request
        Sunny Day 2
        Preconditions:
            Message subject does not contain 'balance'
            Message body contains 'balance'
        Postconditions:
            Function returns True
        """
        def test_is_balance_request_sunny_2(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'asjkldhas'
                body = 'askljdflksadbalancesakldjflksad'
            self.assertTrue(bot_api.is_balance_request(Message))

        """
        Test is_balance_request
        Sunny Day 3
        Preconditions:
            Message subject contains 'balance'
            Message body contains 'balance'
        Postconditions:
            Function returns True
        """
        def test_is_balance_request_sunny_3(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'aasklfjasbalancekjasdflkas'
                body = 'askldfjasdlkfbalancesadkljflasd'
            self.assertTrue(bot_api.is_balance_request(Message))
    
        """
        Test is_balance_request
        Rainy Day
        Preconditions:
            Message subject does not contain 'balance'
            Message body does not contain 'balance'
        Postconditions:
            Function returns False
        """
        def test_is_balance_request_rainy_1(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'asdkfljasdk'
                body = 'asdkfjaklsdf'
            self.assertFalse(bot_api.is_balance_request(Message))

        """
        Test is_help_request
        Sunny Day 1
        Preconditions:
            Message subject contains 'help'
            Message body does not contain 'help'
        Postconditions:
            Function returns True
        """
        def test_is_help_request_sunny_1(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'askljdfalhelpasklfjaslkd'
                body = 'askldfalskd'
            self.assertTrue(bot_api.is_help_request(Message))

        """
        Test is_help_request
        Sunny Day 2
        Preconditions:
            Message subject does not contain 'help'
            Message body contains 'help'
        Postconditions:
            Function returns True
        """
        def test_is_help_request_sunny_2(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'asklkd'
                body = 'askldfhelpalskd'
            self.assertTrue(bot_api.is_help_request(Message))

        """
        Test is_help_request
        Sunny Day 3
        Preconditions:
            Message subject contains 'help'
            Message body contains 'help'
        Postconditions:
            Function returns True
        """
        def test_is_help_request_sunny_3(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'askljdfalhelpasklfjaslkd'
                body = 'askldhelpfalskd'
            self.assertTrue(bot_api.is_help_request(Message))

        """
        Test is_help_request
        Rainy Day 1
        Preconditions:
            Message subject does not contain 'help'
            Message body does not contain 'help'
        Postconditions:
            Function returns True
        """
        def test_is_help_request_sunny_1(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'askljdlfjaslkd'
                body = 'askldfalskd'
            self.assertFalse(bot_api.is_help_request(Message))

        """
        Test contains_iota_amount
        Sunny Day 1
        Preconditions:
            Message body contains '1024 iota'
        Postconditions:
            Function returns True
        """
        def test_contains_iota_amount_sunny_1(self):
            bot_api = api(test_seed)
            class Message:
                body = 'asdfkjlasdlkfj1024 iotaasjldklasd'
            self.assertTrue(bot_api.contains_iota_amount(Message))

        """
        Test contains_iota_amount
        Sunny Day 2
        Preconditions:
            Message body contains '1024 miota'
        Postconditions:
            Function returns True
        """
        def test_contains_iota_amount_sunny_2(self):
            bot_api = api(test_seed)
            class Message:
                body = 'asdfkjlasdlkfj1024 miotaasjldklasd'
            self.assertTrue(bot_api.contains_iota_amount(Message))
    
        """
        Test contains_iota_amount
        Sunny Day 3
        Preconditions:
            Message body contains '1024iota'
        Postconditions:
            Function returns True
        """
        def test_contains_iota_amount_sunny_3(self):
            bot_api = api(test_seed)
            class Message:
                body = 'asdfkjlasdlkfj1024iotaasjldklasd'
            self.assertTrue(bot_api.contains_iota_amount(Message))

        """
        Test contains_iota_amount
        Sunny Day 4
        Preconditions:
            Message body contains '1024miota'
        Postconditions:
            Function returns True
        """
        def test_contains_iota_amount_sunny_4(self):
            bot_api = api(test_seed)
            class Message:
                body = 'asdfkjlasdlkfj1024miotaasjldklasd'
            self.assertTrue(bot_api.contains_iota_amount(Message))

        """
        Test contains_iota_amount
        Rainy Day 1
        Preconditions:
            Message body does not contain and iota amount
        Postconditions:
            Function returns False
        """
        def test_contains_iota_amount_sunny_1(self):
            bot_api = api(test_seed)
            class Message:
                body = 'asdfkjlasdjldklasd'
            self.assertFalse(bot_api.contains_iota_amount(Message))

        """
        Test get_iota_tip_amount
        Sunny Day 1
        Preconditions:
            Message body contains '+1024 iota'
        Postconditions:
            Function returns 1024
        """
        def test_get_iota_tip_amount_sunny_1(self):
            bot_api = api(test_seed)
            class Message:
                body = 'askldjflaksdj+1024 iotaasdfkljas'
            self.assertEqual(bot_api.get_iota_tip_amount(Message),1024)
   
        """
        Test get_iota_tip_amount
        Sunny Day 2
        Preconditions:
            Message body contains '+1024 miota'
        Postconditions:
            Function returns 1024000000
        """
        def test_get_iota_tip_amount_sunny_2(self):
            bot_api = api(test_seed)
            class Message:
                body = 'askldjflaksdj+1024 miotaasdfkljas'
            self.assertEqual(bot_api.get_iota_tip_amount(Message),1024000000)


        """
        Test get_iota_tip_amount
        Sunny Day 3
        Preconditions:
            Message body contains '+1024iota'
        Postconditions:
            Function returns 1024
        """
        def test_get_iota_tip_amount_sunny_3(self):
            bot_api = api(test_seed)
            class Message:
                body = 'askldjflaksdj+1024iotaasdfkljas'
            self.assertEqual(bot_api.get_iota_tip_amount(Message),1024)

        """
        Test get_iota_tip_amount
        Sunny Day 4
        Preconditions:
            Message body contains '+1024miota'
        Postconditions:
            Function returns 1024000000
        """
        def test_get_iota_tip_amount_sunny_4(self):
            bot_api = api(test_seed)
            class Message:
                body = 'askldjflaksdj+1024miotaasdfkljas'
            self.assertEqual(bot_api.get_iota_tip_amount(Message),1024000000)

        """
        Test get_iota_tip_amoun
        Sunny Day 5
        Preconditions:
            Message body contains '+0.01 miota'
        Postconditions:
            Functions returns 10000
        """
        def test_get_iota_tip_amount_sunny_5(self):
            bot_api = api(test_seed)
            class Message:
                body = 'asdkjlfjaslkd+0.01 miotaasdklfjlkasd'
            self.assertEqual(bot_api.get_iota_tip_amount(Message),10000)

        """
        Test get_iota_tip_amoun
        Sunny Day 6
        Preconditions:
            Message body contains '+0.01miota'
        Postconditions:
            Functions returns 10000
        """
        def test_get_iota_tip_amount_sunny_6(self):
            bot_api = api(test_seed)
            class Message:
                body = 'asdkjlfjaslkd+0.01miotaasdklfjlkasd'
            self.assertEqual(bot_api.get_iota_tip_amount(Message),10000)

        """
        Test get_iota_tip_amount
        Rainy Day 1
        Preconditions:
            Message body contains '100 iota +1024 iota'
        Postconditions:
            Function returns 1024
        """
        def test_get_iota_tip_amount_rainy_1(self):
            bot_api = api(test_seed)
            class Message:
                body = 'askldjf100 iota +1024 iotaasdfkljas'
            self.assertEqual(bot_api.get_iota_tip_amount(Message),1024)

        """
        Test get_iota_tip_amount
        Rainy Day 2
        Preconditions:
            Message body contains '100 iota +1024 miota'
        Postconditions:
            Function returns 1024000000
        """
        def test_get_iota_tip_amount_rainy_2(self):
            bot_api = api(test_seed)
            class Message:
                body = 'askldjflaksdj100 iota +1024miotaasdfkljas'
            self.assertEqual(bot_api.get_iota_tip_amount(Message),1024000000)

        """
        Test get_iota_tip_amount
        Rainy Day 3
        Preconditions:
            Message body does not contain a tip amount
        Postconditions:
            Function returns None
        """
        def test_get_iota_tip_amount_rainy_3(self):
            bot_api = api(test_seed)
            class Message:
                body = 'askdlfjaskl'
            self.assertEqual(bot_api.get_iota_tip_amount(Message),None)

        """
        Test get_iota_amount
        Sunny Day 1
        Preconditions:
            Message body contains '1024 iota'
        Postconditions:
            Function returns 1024
        """
        def test_get_iota_amount_sunny_1(self):
            bot_api = api(test_seed)
            class Message:
                body = 'asdlkfjas1024 iota'
            self.assertEqual(bot_api.get_iota_amount(Message),1024)
        
        """
        Test get_iota_amount
        Sunny Day 2
        Preconditions:
            Message body contains '1024 miota'
        Postconditions:
            Function returns 1024000000
        """
        def test_get_iota_amount_sunny_2(self):
            bot_api = api(test_seed)
            class Message:
                body = 'asdlkfjas1024 miota'
            self.assertEqual(bot_api.get_iota_amount(Message),1024000000)

        """
        Test get_iota_amount
        Sunny Day 3
        Preconditions:
            Message body contains '1024iota'
        Postconditions:
            Function returns 1024
        """
        def test_get_iota_amount_sunny_3(self):
            bot_api = api(test_seed)
            class Message:
                body = 'asdlkfjas1024iota'
            self.assertEqual(bot_api.get_iota_amount(Message),1024)

        """
        Test get_iota_amount
        Sunny Day 4
        Preconditions:
            Message body contains '1024miota'
        Postconditions:
            Function returns 1024000000
        """
        def test_get_iota_amount_sunny_4(self):
            bot_api = api(test_seed)
            class Message:
                body = 'asdlkfjas1024miota'
            self.assertEqual(bot_api.get_iota_amount(Message),1024000000)

        """
        Test get_iota_amount
        Rainy Day 1
        Preconditions:
            Message body does not contain an iota amount
        Postconditions:
            Function returns None
        """
        def test_get_iota_amount_rainy_1(self):
            bot_api = api(test_seed)
            class Message:
                body = 'asdklfjhaslkdf'
            self.assertEqual(bot_api.get_iota_amount(Message),None)

        """
        Test get_message_address
        Sunny Day 1
        Preconditions:
            Message body contains 'A'*90
        Preconditions:
            Function returns 'A'*90
        """
        def test_get_message_address_sunny_1(self):
            bot_api = api(test_seed)
            class Message:
                body = 'A'*90
            self.assertEqual(bot_api.get_message_address(Message),bytearray('A'*90,'utf-8'))

        """
        Test get_message_address
        Rainy Day 1
        Preconditions:
            Message body does not contain an address
        Preconditions:
            Function returns None
        """
        def test_get_message_address_rainy_1(self):
            bot_api = api(test_seed)
            class Message:
                body = 'asdflkjasdklf'
            self.assertEqual(bot_api.get_message_address(Message),None)

        """
        Test is_tip
        Sunny Day 1
        Preconditions:
            Message body contains '+1024 iota'
        Postconditions:
            Function returns True
        """
        def test_is_tip_sunny_1(self):
            bot_api = api(test_seed)
            class Comment:
                body = 'sadklfjasdlk+1024 iotaasdfkljasld'  
            self.assertTrue(bot_api.is_tip(Comment))

        """
        Test is_tip
        Sunny Day 2
        Preconditions:
            Message body contains '+1024iota'
        Postconditions:
            Function returns True
        """
        def test_is_tip_sunny_2(self):
            bot_api = api(test_seed)
            class Comment:
                body = 'sadklfjasdlk+1024iotaasdfkljasld'  
            self.assertTrue(bot_api.is_tip(Comment))

        """
        Test is_tip
        Sunny Day 3
        Preconditions:
            Message body contains '+1024 miota'
        Postconditions:
            Function returns True
        """
        def test_is_tip_sunny_3(self):
            bot_api = api(test_seed)
            class Comment:
                body = 'sadklfjasdlk+1024 miotaasdfkljasld'  
            self.assertTrue(bot_api.is_tip(Comment))

        """
        Test is_tip
        Sunny Day 4
        Preconditions:
            Message body contains '+1024miota'
        Postconditions:
            Function returns True
        """
        def test_is_tip_sunny_4(self):
            bot_api = api(test_seed)
            class Comment:
                body = 'sadklfjasdlk+1024miotaasdfkljasld'  
            self.assertTrue(bot_api.is_tip(Comment))

        """
        Test is_tip
        Sunny Day 5
        Preconditions:
            Message body contains '+0.01 miota'
        Postconditions:
            Function returns True
        """
        def test_is_tip_sunny_5(self):
            bot_api = api(test_seed)
            class Comment:
                body = 'aslkdjfslakdjf+0.01 miotaklajsdklfa'
            self.assertTrue(bot_api.is_tip(Comment))

        """
        Test is_tip
        Sunny Day 6
        Preconditions:
            Message body contains '+0.01miota'
        Postconditions:
            Function returns True
        """
        def test_is_tip_sunny_6(self):
            bot_api = api(test_seed)
            class Comment:
                body = 'aslkdjfslakdjf+0.01miotaklajsdklfa'
            self.assertTrue(bot_api.is_tip(Comment))


        """
        Test is_tip
        Rainy Day 1
        Preconditions:
            Message body does not contain a tip
        Postconditions:
            Function returns False
        """
        def test_is_tip_rainy_1(self):
            bot_api = api(test_seed)
            class Comment:
                body = 'asdklfjaskljfas'
            self.assertFalse(bot_api.is_tip(Comment))

        """
        Test is_donation_request
        Sunny Day 1
        Preconditions:
            Message subject contains 'donation'
            Message body does not contain 'dontation'
        Postconditions:
            Function returns True
        """
        def test_is_donation_request_sunny_1(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'kljasjdfklasdonatelkas;jdfas'
                body = 'askdlfjasdlk'
            self.assertTrue(bot_api.is_donation_request(Message))

        """
        Test is_donation_request
        Sunny Day 2
        Preconditions:
            Message subject does not contain 'donation'
            Message body contains 'dontation'
        Postconditions:
            Function returns True
        """
        def test_is_donation_request_sunny_2(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'kljasjdfkllkas;jdfas'
                body = 'askdlfjasdonatedlk'
            self.assertTrue(bot_api.is_donation_request(Message))
                
        """
        Test is_donation_request
        Sunny Day 3
        Preconditions:
            Message subject contains 'donation'
            Message body contains 'dontation'
        Postconditions:
            Function returns True
        """
        def test_is_donation_request_sunny_3(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'kljasjdfklasdonatelkas;jdfas'
                body = 'askdlfjdonateasdlk'
            self.assertTrue(bot_api.is_donation_request(Message))

        """
        Test is_donation_request
        Rainy Day 1
        Preconditions:
            Message subject does not contain 'donation'
            Message body does not contain 'dontation'
        Postconditions:
            Function returns False
        """
        def test_is_donation_request_sunny_1(self):
            bot_api = api(test_seed)
            class Message:
                subject = 'kljasjdfklaslkas;jdfas'
                body = 'askdlfjasdlk'
            self.assertFalse(bot_api.is_donation_request(Message))

        """
        Test add_new_user
        Sunny Day 1
        Preconditions:
            'testDB.db' database is initialized
            'TestUser123' does not exist in the database
        Postconditions:
            User exists in the database
        """
        def test_add_new_user_sunny_1(self):
            username = 'TestUser123'
            bot_db = Database('test_db.db')
            bot_db.add_new_user(username)

        """
        Test set_balance
        Sunny Day 1
        Preconditions:
            None
        Postconditions:
            User balance is 10
        """
        def test_set_balance_sunny_1(self):
            username = 'TestUser123'
            bot_db = Database('test_db.db')
            bot_db.set_balance(username,10)
            self.assertEqual(bot_db.get_user_balance(username),10)

        """
        Test add_balance
        Sunny Day 1
        Preconditions:
            None
        Postconditions:
            Balance is 10 greater than it was
        """
        def test_add_balance_sunny_1(self):
            bot_db = Database('test_db.db')
            username = 'TestUser123'
            starting_balance = bot_db.get_user_balance(username)
            bot_db.add_balance(username,10)
            self.assertEqual(bot_db.get_user_balance(username),starting_balance + 10)
            
        """
        Test subtract_balance
        Sunny Day 1
        Preconditions:
            None
        Postconditions:
            Balance is 10 less than it was
        """
        def test_subtract_balance_sunny_1(self):
            bot_db = Database('test_db.db')
            username = 'TestUser123'
            starting_balance = bot_db.get_user_balance(username)
            bot_db.subtract_balance(username,10)
            self.assertEqual(bot_db.get_user_balance(username),starting_balance - 10)

        """
        Test check_balance
        Sunny Day 1
        Preconditions:
            User has balance of 50
        Postconditions:
            Function returns True
        """
        def test_check_balance_sunny_1(self):
            bot_db = Database('test_db.db')
            username = 'TestUser123'
            bot_db.set_balance(username,50)
            self.assertTrue(bot_db.check_balance(username,25))

        """
        Test check_balance
        Sunny Day 2
        Preconditions:
            User has balance of 50
        Postconditions:
            Function returns True
        """
        def test_check_balance_sunny_2(self):
            bot_db = Database('test_db.db')
            username = 'TestUser123'
            bot_db.set_balance(username,50)
            self.assertTrue(bot_db.check_balance(username,50))

        """
        Test check_balance
        Rainy Day 1
        Preconditions:
            User has a balance of 50
        Postconditions:
            Function returns False
        """
        def test_check_balance_rainy_1(self):
            bot_db = Database('test_db.db')
            username = 'TestUser123'
            bot_db.set_balance(username, 50)
            self.assertFalse(bot_db.check_balance(username,100))

        """
        Test get_user_balance
        Sunny Day 1
        Preconditions:
            User has a balance of 50
        Postconditions:
            Function returns 50
        """
        def test_get_user_balance_sunny_1(self):
            bot_db = Database('test_db.db')
            username = 'TestUser123'
            bot_db.set_balance(username,50)
            self.assertEqual(bot_db.get_user_balance(username),50)

        """
        Test get_iota_value
        Sunny 1
        Preconditions:
            iota amount is 10000
        Postconditions:
            function returns the proper value
        """
        def test_get_iota_value_sunny_1(self):
            bot_api = api(test_seed)
            amount = 10000
            value = bot_api.get_iota_value(10000)
            print('Value is: ${0}'.format(value))

        """
        Test set_head_index
        Sunny 1
        Preconditions:
            Database table indecies exists with a single entry with primary key 0
        Postconditions:
            indecies.head is set to 1500
        """
        def test_set_head_index_sunny_1(self):
            bot_db = Database('test_db.db')
            bot_db.set_head_index(1500)
            self.assertEqual(bot_db.db.execute("SELECT head FROM indicies WHERE key=0").fetchone()[0],1500)

        """
        Test get_head_index
        Sunny 1
        Preconditions:
            Database table indicies exists with a single entry with primary key 0
            indicies.head is set to 2500
        Postconditions:
            get_head_index returns 2500
        """
        def test_get_head_index_sunny_1(self):
            bot_db = Database('test_db.db')
            bot_db.db.execute("UPDATE indicies SET head=2500 WHERE key=0")
            bot_db.conn.commit()
            self.assertEqual(bot_db.get_head_index(),2500)

        """
        Test set_tail_index
        Sunny 1
        Preconditions:
            Database table indecies exists with a single entry with primary key 0
        Postconditions:
            indecies.tail is set to 3000
        """
        def test_set_head_index_sunny_1(self):
            bot_db = Database('test_db.db')
            bot_db.set_tail_index(3000)
            self.assertEqual(bot_db.db.execute("SELECT tail FROM indicies WHERE key=0").fetchone()[0],3000)

        """
        Test get_tail_index
        Sunny 1
        Preconditions:
            Database table indicies exists with a single entry with primary key 0
            indicies.tail is set to 7000
        Postconditions:
            get_tail_index returns 7000
        """
        def test_get_tail_index_sunny_1(self):
            bot_db = Database('test_db.db')
            bot_db.db.execute("UPDATE indicies SET tail=7000 WHERE key=0")
            bot_db.conn.commit()
            self.assertEqual(bot_db.get_tail_index(),7000)

        """
        Test incriment_head_index
        Sunny 1
        Preconditions:
            Database table indicies exists with a single entry with primary key 0
            indicies.head is set to 1400
        Postconditions:
            indicies.head is 1401
        """
        def test_incriment_head_index_sunny_1(self):
            bot_db = Database('test_db.db')
            bot_db.db.execute("UPDATE indicies SET head=1400 WHERE key=0")
            bot_db.conn.commit()
            bot_db.incriment_head_index()
            self.assertEqual(bot_db.db.execute("SELECT head FROM indicies WHERE key=0").fetchone()[0],1401)

unittest.main()
