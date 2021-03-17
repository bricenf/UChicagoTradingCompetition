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


option_strikes = [90, 95, 100, 105, 110]

prices = [] #all of the prices as time goes on
price_SD = [] #standard deviations as it goes on (list of the difference between current price and the mean up until that point)

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

    def compute_vol_estimate(self, price: float) -> float:
        #vol = self.compute_vol_estimate(self.underlying_price,strike,time_to_expiry)

        """
        This function is used to provide an estimate of underlying's volatility. Because this is
        an example bot, we just use a placeholder value here. We recommend that you look into
        different ways of finding what the true volatility of the underlying is.
        """

        #calculate volatility
        #https://www.investopedia.com/terms/v/volatility.asp
        prices.append(price)

        #Find the mean
        mean_of_prices = sum(prices) / len(prices)

        standard_deviaiton = price - mean_of_prices #standard deviation between current price and historic mean
        standard_deviation = standard_deviaiton ** 2

        price_SD.append(standard_deviation)
        price_SD = map(float,price_SD)

        volatility = sum(map(float,standard_deviaiton)) / len(prices)
        print(volatility)


        return 0.35

    def compute_options_price(self,flag: str,underlying_px: float,strike_px: float,time_to_expiry: float,volatility: float,) -> float:
        """
        This function should compute the price of an option given the provided parameters. Some
        important questions you may want to think about are:
            - What are the units associated with each of these quantities?
            - What formula should you use to compute the price of the option?
            - Are there tricks you can use to do this more quickly?
        You may want to look into the py_vollib library, which is installed by default in your
        virtual environment.
        """
        return 1.0



    async def update_options_quotes(self): #This function will update the quotes that the bot has currently put into the market.

        # What should this value actually be?
        time_to_expiry = 21 / 252
        vol = self.compute_vol_estimate(self.underlying_price)

        for strike in option_strikes:
            for flag in ["C", "P"]:
                asset_name = f"UC{strike}{flag}"
                theo = self.compute_options_price(
                    flag, self.underlying_price, strike, time_to_expiry, vol
                )

                bid_response = await self.place_order(
                    asset_name,
                    pb.OrderSpecType.LIMIT,
                    pb.OrderSpecSide.BID,
                    1,  # How should this quantity be chosen?
                    theo - 0.30,  # How should this price be chosen?
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
            book = update.market_snapshot_msg.books["UC"]

            # Compute the mid price of the market and store it
            self.underlying_price = (float(book.bids[0].px) + float(book.asks[0].px)) / 2

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
