#!/usr/bin/env python
"""
python clients\Case2V1.py

"""
from dataclasses import astuple
from utc_bot import UTCBot, start_bot
import proto.utc_bot as pb
import betterproto

import asyncio
import random

"""
0 = UC (Underlying)

1 = UC90C
2 = UC90P

3 = UC95C
4 = UC95P

5 = UC100C
6 = UC100P

7 = UC105C
8 = UC105P

9 = UC110C
10 = UC110P

"""

option_strikes = [90, 95, 100, 105, 110]

prices0 = [] #all of the prices as time goes on
prices1 = []
prices2 = []
prices3 = []
prices4 = []
prices5 = []
prices6 = []
prices7 = []
prices8 = []
prices9 = []
prices10 = []

prices_SD0 = [] #standard deviations as it goes on (list of the difference between current price and the mean up until that point)
prices_SD1 = []
prices_SD2 = []
prices_SD3 = []
prices_SD4 = []
prices_SD5 = []
prices_SD6 = []
prices_SD7 = []
prices_SD8 = []
prices_SD9 = []
prices_SD10 = []

volatility_array0 = []
volatility_array1 = []
volatility_array2 = []
volatility_array3 = []
volatility_array4 = []
volatility_array5 = []
volatility_array6 = []
volatility_array7 = []
volatility_array8 = []
volatility_array9 = []
volatility_array10 = []

time = [] #array of time

class Case2ExampleBot(UTCBot):
    async def handle_round_started(self):
        self.positions = {}
        self.positions["UC"] = 0
        for strike in option_strikes:
            for flag in ["C", "P"]:
                self.positions[f"UC{strike}{flag}"] = 0

        # Stores the current day (starting from 0 and ending at 5). This is a floating point number, meaning that it includes information about partial days
        self.current_day = 0
        # Stores the current value of the underlying asset
        self.underlying_price = 100

    #update arrays

    def compute_vol_estimate(self, price: float, number) -> float:
        def prices(value,number):
            if number == 0:
                prices0.append(value)
            if number == 1:
                prices1.append(value)
            if number == 2:
                prices2.append(value)
            if number == 3:
                prices3.append(value)
            if number == 4:
                prices4.append(value)
            if number == 5:
                prices5.append(value)
            if number == 6:
                prices6.append(value)
            if number == 7:
                prices7.append(value)
            if number == 8:
                prices8.append(value)
            if number == 9:
                prices9.append(value)
            if number == 10:
                prices10.append(value)
        def pricesSD(value,number):
            if number == 0:
                prices_SD0.append(value)
            if number == 1:
                prices_SD1.append(value)
            if number == 2:
                prices_SD2.append(value)
            if number == 3:
                prices_SD3.append(value)
            if number == 4:
                prices_SD4.append(value)
            if number == 5:
                prices_SD5.append(value)
            if number == 6:
                prices_SD6.append(value)
            if number == 7:
                prices_SD7.append(value)
            if number == 8:
                prices_SD8.append(value)
            if number == 9:
                prices_SD9.append(value)
            if number == 10:
                prices_SD10.append(value)
        def volatility_array(value,number):
            if number == 0:
                volatility_array0.append(value)
            if number == 1:
                volatility_array1.append(value)
            if number == 2:
                volatility_array2.append(value)
            if number == 3:
                volatility_array3.append(value)
            if number == 4:
                volatility_array4.append(value)
            if number == 5:
                volatility_array5.append(value)
            if number == 6:
                volatility_array6.append(value)
            if number == 7:
                volatility_array7.append(value)
            if number == 8:
                volatility_array8.append(value)
            if number == 9:
                volatility_array9.append(value)
            if number == 10:
                volatility_array10.append(value)
        global prices_SD
        #calculate volatility
        #https://www.investopedia.com/terms/v/volatility.asp
        #update arrays
        prices(price,number)

        #Find the mean
        if number == 0:
            mean_of_prices = sum(prices0) / len(prices0)
            standard_deviaiton = price - mean_of_prices #standard deviation between current price and historic mean
            standard_deviation = standard_deviaiton ** 2
            prices_SD0.append(standard_deviation)
            volatility = sum(prices_SD0) / len(prices_SD0)
            volatility_array0.append(volatility)
        if number == 1:
            mean_of_prices = sum(prices1) / len(prices1)
            standard_deviaiton = price - mean_of_prices1 #standard deviation between current price and historic mean
            standard_deviation = standard_deviaiton ** 2
            prices_SD1.append(standard_deviation)
            volatility = sum(prices_SD0) / len(prices_SD1)
            volatility_array1.append(volatility)
        if number == 2:
            mean_of_prices = sum(prices2) / len(prices2)
            standard_deviaiton = price - mean_of_prices #standard deviation between current price and historic mean
            standard_deviation = standard_deviaiton ** 2
            prices_SD2.append(standard_deviation)
            volatility = sum(prices_SD0) / len(prices_SD2)
            volatility_array2.append(volatility)
        if number == 3:
            mean_of_prices = sum(prices3) / len(prices3)
            standard_deviaiton = price - mean_of_prices #standard deviation between current price and historic mean
            standard_deviation = standard_deviaiton ** 2
            prices_SD3.append(standard_deviation)
            volatility = sum(prices_SD3) / len(prices_SD3)
            volatility_array3.append(volatility)
        if number == 4:
            mean_of_prices = sum(prices4) / len(prices4)
            standard_deviaiton = price - mean_of_prices #standard deviation between current price and historic mean
            standard_deviation = standard_deviaiton ** 2
            prices_SD4.append(standard_deviation)
            volatility = sum(prices_SD4) / len(prices_SD4)
            volatility_array4.append(volatility)
        if number == 5:
            mean_of_prices = sum(prices5) / len(prices5)
            standard_deviaiton = price - mean_of_prices #standard deviation between current price and historic mean
            standard_deviation = standard_deviaiton ** 2
            prices_SD5.append(standard_deviation)
            volatility = sum(prices_SD5) / len(prices_SD5)
            volatility_array5.append(volatility)
        if number == 6:
            mean_of_prices = sum(prices6) / len(prices6)
            standard_deviaiton = price - mean_of_prices #standard deviation between current price and historic mean
            standard_deviation = standard_deviaiton ** 2
            prices_SD6.append(standard_deviation)
            volatility = sum(prices_SD6) / len(prices_SD6)
            volatility_array6.append(volatility)
        if number == 7:
            mean_of_prices = sum(prices7) / len(prices7)
            standard_deviaiton = price - mean_of_prices #standard deviation between current price and historic mean
            standard_deviation = standard_deviaiton ** 2
            prices_SD7.append(standard_deviation)
            volatility = sum(prices_SD7) / len(prices_SD7)
            volatility_array7.append(volatility)
        if number == 8:
            mean_of_prices = sum(prices8) / len(prices8)
            standard_deviaiton = price - mean_of_prices #standard deviation between current price and historic mean
            standard_deviation = standard_deviaiton ** 2
            prices_SD8.append(standard_deviation)
            volatility = sum(prices_SD8) / len(prices_SD8)
            volatility_array8.append(volatility)
        if number == 9:
            mean_of_prices = sum(prices9) / len(prices9)
            standard_deviaiton = price - mean_of_prices #standard deviation between current price and historic mean
            standard_deviation = standard_deviaiton ** 2
            prices_SD9.append(standard_deviation)
            volatility = sum(prices_SD9) / len(prices_SD9)
            volatility_array9.append(volatility)
        if number == 10:
            mean_of_prices = sum(prices10) / len(prices10)
            standard_deviaiton = price - mean_of_prices #standard deviation between current price and historic mean
            standard_deviation = standard_deviaiton ** 2
            prices_SD10.append(standard_deviation)
            volatility = sum(prices_SD10) / len(prices_SD10)
            volatility_array10.append(volatility)


        #print("priceing is is: ",price)
        print("Volatility with: ",volatility)
        return .3

    def compute_options_price1(self,flag: str,underlying_px: float,strike_px: float,time_to_expiry: float,volatility: float,) -> float:
        #HOW DO YOU CALCULATE STRIKE PRICE

        """
        This function should compute the price of an option given the provided parameters. Some
        important questions you may want to think about are:
            - What are the units associated with each of these quantities?
            - What formula should you use to compute the price of the option?
            - Are there tricks you can use to do this more quickly?
        You may want to look into the py_vollib library, which is installed by default in your
        virtual environment.
        """




        return -1.0



    async def update_options_quotes(self): #This function will update the quotes that the bot has currently put into the market.

        # What should this value actually be?
        time_to_expiry = current_day + 21 / 252
        vol_underlying0 = self.compute_vol_estimate(self.underlying_price0,0)
        vol_underlying1 = self.compute_vol_estimate(self.underlying_price1,1)
        vol_underlying2 = self.compute_vol_estimate(self.underlying_price2,2)
        vol_underlying3 = self.compute_vol_estimate(self.underlying_price3,3)
        vol_underlying4 = self.compute_vol_estimate(self.underlying_price4,4)
        vol_underlying5 = self.compute_vol_estimate(self.underlying_price5,5)
        vol_underlying6 = self.compute_vol_estimate(self.underlying_price6,6)
        vol_underlying7 = self.compute_vol_estimate(self.underlying_price7,7)
        vol_underlying8 = self.compute_vol_estimate(self.underlying_price8,8)
        vol_underlying9 = self.compute_vol_estimate(self.underlying_price9,9)
        vol_underlying10 = self.compute_vol_estimate(self.underlying_price10,10)

        for strike in option_strikes:
            for flag in ["C", "P"]:
                asset_name = f"UC{strike}{flag}"
                theo = self.compute_options_price1(flag, self.underlying_price1, strike, time_to_expiry, vol_underlying1) #HOW DO YOU CALCULATE STRICK PRICE

                bid_response = await self.place_order(
                    asset_name,
                    pb.OrderSpecType.LIMIT,
                    pb.OrderSpecSide.BID,
                    1,  # How should this quantity be chosen?
                    theo - 0.30,  # How should this price be chosen? THEO IS THE BLACKSCHOLES PRICING
                )
                assert bid_response.ok

                ask_response = await self.place_order(
                    asset_name,
                    pb.OrderSpecType.LIMIT,
                    pb.OrderSpecSide.ASK,
                    1,
                    theo + 0.30,
                )
                assert ask_response.ok

    async def handle_exchange_update(self, update: pb.FeedMessage):
        kind, _ = betterproto.which_one_of(update, "msg")

        if kind == "pnl_msg":
            # When you hear from the exchange about your PnL, print it out

            print("My PnL:", update.pnl_msg.m2m_pnl)


        elif kind == "fill_msg":
            # When you hear about a fill you had, update your positions
            fill_msg = update.fill_msg

            if fill_msg.order_side == pb.FillMessageSide.BUY:
                self.positions[fill_msg.asset] += update.fill_msg.filled_qty
            else:
                self.positions[fill_msg.asset] -= update.fill_msg.filled_qty

        elif kind == "market_snapshot_msg":
            # When we receive a snapshot of what's going on in the market, update our information
            # about the underlying price.
            book0 = update.market_snapshot_msg.books["UC"]
            book1 = update.market_snapshot_msg.books["UC90C"]
            book2 = update.market_snapshot_msg.books["UC90P"]
            book3 = update.market_snapshot_msg.books["UC95C"]
            book4 = update.market_snapshot_msg.books["UC95P"]
            book5 = update.market_snapshot_msg.books["UC100C"]
            book6 = update.market_snapshot_msg.books["UC100P"]
            book7 = update.market_snapshot_msg.books["UC105C"]
            book8 = update.market_snapshot_msg.books["UC105P"]
            book9 = update.market_snapshot_msg.books["UC110C"]
            book10 = update.market_snapshot_msg.books["UC110P"]

            # Compute the mid price of the market and store it
            self.underlying_price0 = (float(book0.bids[0].px) + float(book0.asks[0].px)) / 2
            self.underlying_price1 = (float(book1.bids[0].px) + float(book1.asks[0].px)) / 2
            self.underlying_price2 = (float(book2.bids[0].px) + float(book2.asks[0].px)) / 2
            self.underlying_price3 = (float(book3.bids[0].px) + float(book3.asks[0].px)) / 2
            self.underlying_price4 = (float(book4.bids[0].px) + float(book4.asks[0].px)) / 2
            self.underlying_price5 = (float(book5.bids[0].px) + float(book5.asks[0].px)) / 2
            self.underlying_price6 = (float(book6.bids[0].px) + float(book6.asks[0].px)) / 2
            self.underlying_price7 = (float(book7.bids[0].px) + float(book7.asks[0].px)) / 2
            self.underlying_price8 = (float(book8.bids[0].px) + float(book8.asks[0].px)) / 2
            self.underlying_price9 = (float(book9.bids[0].px) + float(book9.asks[0].px)) / 2
            self.underlying_price10 = (float(book10.bids[0].px) + float(book10.asks[0].px)) / 2
            await self.update_options_quotes()

        elif (kind == "generic_msg" and update.generic_msg.event_type == pb.GenericMessageType.MESSAGE):
            # The platform will regularly send out what day it currently is (starting from day 0 at
            # the start of the case)
            self.current_day = float(update.generic_msg.message)

        elif kind == "trade_msg":
            # There are other pieces of information the exchange provides feeds for. See if you can
            # find ways to use them to your advantage (especially when more than one competitor is
            # in the market)
            pass


if __name__ == "__main__":
    start_bot(Case2ExampleBot)
