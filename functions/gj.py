# from binance.lib.utils import check_required_parameter
# from binance.lib.utils import check_required_parameters
# from binance.lib.utils import check_enum_parameter
# from binance.lib.enums import TransferType
# from binance.spot import Spot as Client
# from environs import Env
# import binance 

# env = Env()
# env.read_env()

# api_key = env.str('BINANCE_KEY')
# api_secret = env.str('BINANCE_SECRET_KEY')


# def system_status(self):
#     """System Status (System)
#     Fetch system status.
#     GET /sapi/v1/system/status
#     https://binance-docs.github.io/apidocs/spot/en/#system-status-sapi-system
#     """

#     return self.query("/sapi/v1/system/status")


# def coin_info(self, **kwargs):
#     """All Coins' Information (USER_DATA)
#     Get information of coins (available for deposit and withdraw) for user.
#     GET /sapi/v1/capital/config/getall
#     https://binance-docs.github.io/apidocs/spot/en/#all-coins-39-information-user_data
#     Keyword Args:
#         recvWindow (int, optional): The value cannot be greater than 60000
#     """

#     return self.sign_request("GET", "/sapi/v1/capital/config/getall", kwargs)


# def account_snapshot(self, type: str, **kwargs):
#     check_required_parameter(type, "type")
#     payload = {"type": type, **kwargs}
#     return self.sign_request("GET", "/sapi/v1/accountSnapshot", payload)


# def disable_fast_withdraw(self, **kwargs):
#     return self.sign_request(
#         "POST", "/sapi/v1/account/disableFastWithdrawSwitch", kwargs
#     )


# def enable_fast_withdraw(self, **kwargs):


#     return self.sign_request(
#         "POST", "/sapi/v1/account/enableFastWithdrawSwitch", kwargs
#     )


# def withdraw(self, coin: str, amount: float, address: str, **kwargs):

#     check_required_parameters(
#         [[coin, "coin"], [amount, "amount"], [address, "address"]]
#     )
#     payload = {"coin": coin, "amount": amount, "address": address, **kwargs}
#     return self.sign_request("POST", "/sapi/v1/capital/withdraw/apply", payload)


# def deposit_history(self, **kwargs):
#     return self.sign_request("GET", "/sapi/v1/capital/deposit/hisrec", kwargs)


# def withdraw_history(self, **kwargs):
#     return self.sign_request("GET", "/sapi/v1/capital/withdraw/history", kwargs)


# def deposit_address(self, coin: str, **kwargs):
#     check_required_parameter(coin, "coin")
#     payload = {"coin": coin, **kwargs}
#     return self.sign_request("GET", "/sapi/v1/capital/deposit/address", payload)


# def account_status(self, **kwargs):

#     return self.sign_request("GET", "/sapi/v1/account/status", kwargs)


# def api_trading_status(self, **kwargs):

#     return self.sign_request("GET", "/sapi/v1/account/apiTradingStatus", kwargs)


# def dust_log(self, **kwargs):
  

#     return self.sign_request("GET", "/sapi/v1/asset/dribblet", kwargs)


# def user_universal_transfer(self, type: str, asset: str, amount: str, **kwargs):
#     """User Universal Transfer (USER_DATA)
#     POST /sapi/v1/asset/transfer
#     https://binance-docs.github.io/apidocs/spot/en/#user-universal-transfer-user_data
#     Args:
#         type (str)
#         asset (str)
#         amount (str)
#     Keyword Args:
#         fromSymbol (str, optional): Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
#         toSymbol (str, optional): Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
#         recvWindow (int, optional): The value cannot be greater than 60000
#     """
#     check_required_parameters([[type, "type"], [asset, "asset"], [amount, "amount"]])
#     check_enum_parameter(type, TransferType)
#     payload = {"type": type, "asset": asset, "amount": amount, **kwargs}
#     return self.sign_request("POST", "/sapi/v1/asset/transfer", payload)


# def user_universal_transfer_history(self, type: str, **kwargs):
#     """Query User Universal Transfer History (USER_DATA)
#     GET /sapi/v1/asset/transfer
#     https://binance-docs.github.io/apidocs/spot/en/#query-user-universal-transfer-history-user_data
#      Args:
#         type (str)
#      Keyword Args:
#         startTime (int, optional)
#         endTime (int, optional)
#         current (int, optional): Default 1
#         size (int, optional): Default 10, Max 100
#         fromSymbol (str, optional): Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
#         toSymbol (str, optional): Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
#         recvWindow (int, optional): The value cannot be greater than 60000
#     """
#     check_required_parameter(type, "type")
#     check_enum_parameter(type, TransferType)
#     payload = {"type": type, **kwargs}
#     return self.sign_request("GET", "/sapi/v1/asset/transfer", payload)


# def transfer_dust(self, asset, **kwargs):
#     """Dust Transfer (USER_DATA)
#     Convert dust assets to BNB.
#     POST /sapi/v1/asset/dust
#     https://binance-docs.github.io/apidocs/spot/en/#dust-transfer-user_data
#     Args:
#         asset (str)
#     Keyword Args:
#         recvWindow (int, optional): The value cannot be greater than 60000
#     """

#     check_required_parameter(asset, "asset")
#     payload = {"asset": asset, **kwargs}

#     return self.sign_request("POST", "/sapi/v1/asset/dust", payload)


# def asset_dividend_record(self, **kwargs):
#     """Asset Dividend Record (USER_DATA)
#     Query asset dividend record.
#     GET /sapi/v1/asset/assetDividend
#     https://binance-docs.github.io/apidocs/spot/en/#asset-dividend-record-user_data
#     Keyword Args:
#         asset (str, optional)
#         startTime (int, optional)
#         endTime (int, optional)
#         limit (int, optional): Default 20, max 500
#         recvWindow (int, optional): The value cannot be greater than 60000
#     """

#     return self.sign_request("GET", "/sapi/v1/asset/assetDividend", kwargs)


# def asset_detail(self, **kwargs):
#     """Asset Detail (USER_DATA)
#     Fetch details of assets supported on Binance.
#     GET /sapi/v1/asset/assetDetail
#     https://binance-docs.github.io/apidocs/spot/en/#asset-detail-sapi-user_data
#     Keyword Args:
#         recvWindow (int, optional): The value cannot be greater than 60000
#     """

#     return self.sign_request("GET", "/sapi/v1/asset/assetDetail", kwargs)


# def trade_fee(self, **kwargs):
#     """Trade Fee (USER_DATA)
#     Fetch trade fee, values in percentage.
#     GET /sapi/v1/asset/tradeFee
#     https://binance-docs.github.io/apidocs/spot/en/#trade-fee-sapi-user_data
#     Keyword Args:
#         symbol (str, optional)
#         recvWindow (int, optional): The value cannot be greater than 60000
#     """

#     return self.sign_request("GET", "/sapi/v1/asset/tradeFee", kwargs)


# def funding_wallet(self, **kwargs):
#     """Funding Wallet (USER_DATA)
#     POST /sapi/v1/asset/get-funding-asset
#     https://binance-docs.github.io/apidocs/spot/en/#funding-wallet-user_data
#     Keyword Args:
#         asset (str, optional)
#         needBtcValuation (str, optional): true or false
#         recvWindow (int, optional): The value cannot be greater than 60000
#     """

#     return self.sign_request("POST", "/sapi/v1/asset/get-funding-asset", kwargs)


# def user_asset(self, **kwargs):
#     """User Asset (USER_DATA)
#     Get user assets, just for positive data.
#     Weight(IP): 5
#     POST /sapi/v3/asset/getUserAsset
#     https://binance-docs.github.io/apidocs/spot/en/#user-asset-user_data
#     Keyword Args:
#         asset (str, optional): If asset is blank, then query all positive assets user have.
#         needBtcValuation (str, optional)
#         recvWindow (int, optional): The value cannot be greater than 60000
#     """

#     url_path = "/sapi/v3/asset/getUserAsset"
#     return self.sign_request("POST", url_path, {**kwargs})


# def api_key_permissions(self, **kwargs):
#     """Get API Key Permission (USER_DATA)
#     GET /sapi/v1/account/apiRestrictions
#     https://binance-docs.github.io/apidocs/spot/en/#get-api-key-permission-user_data
#     Keyword Args:
#         recvWindow (int, optional): The value cannot be greater than 60000
#     """

#     return self.sign_request("GET", "/sapi/v1/account/apiRestrictions", kwargs)


# def bnb_convertible_assets(self, **kwargs):
#     """Get Assets That Can Be Converted Into BNB (USER_DATA)
#     POST /sapi/v1/asset/dust-btc
#     https://binance-docs.github.io/apidocs/spot/en/#get-assets-that-can-be-converted-into-bnb-user_data
#     Keyword Args:
#         recvWindow (int, optional): The value cannot be greater than 60000
#     """

#     return self.sign_request("POST", "/sapi/v1/asset/dust-btc", kwargs)


# def convertible_coins(self, **kwargs):
#     """Query auto-converting stable coins (USER_DATA)
#     GET /sapi/v1/capital/contract/convertible-coins
#     https://binance-docs.github.io/apidocs/spot/en/#query-auto-converting-stable-coins-user_data
#     """

#     return self.sign_request(
#         "GET", "/sapi/v1/capital/contract/convertible-coins", kwargs
#     )


# def toggle_auto_convertion(self, coin: str, enable: bool, **kwargs):
#     """Toggle auto-converting stable coins (USER_DATA)
#     POST /sapi/v1/capital/contract/convertible-coins
#     https://binance-docs.github.io/apidocs/spot/en/#switch-on-off-busd-and-stable-coins-conversion-user_data
#     """

#     check_required_parameters([[coin, "symbol"], [enable, "enable"]])

#     payload = {"coin": coin, "enable": enable, **kwargs}
#     return self.sign_request(
#         "POST", "/sapi/v1/capital/contract/convertible-coins", payload
#     )


# def cloud_mining_trans_history(self, startTime: int, endTime: int, **kwargs):
#     """Get Cloud-Mining payment and refund history (USER_DATA)
#     GET /sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage
#     https://binance-docs.github.io/apidocs/spot/en/#get-cloud-mining-payment-and-refund-history-user_data
#     Args:
#         startTime (int)
#         endTime (int)
#     Keyword Args:
#         tranId (int, optional)
#         clientTranId (str, optional)
#         asset (str, optional)
#         current (int, optional): Default Value: 1
#         size (int, optional): Default Value: 100; Max Value: 100
#         recvWindow (int, optional)
#     """

#     check_required_parameters([[startTime, "startTime"], [endTime, "endTime"]])

#     url_path = "/sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage"
#     payload = {"startTime": startTime, "endTime": endTime, **kwargs}
#     return self.sign_request("GET", url_path, payload)


# def convert_transfer(
#     self, clientTranId: str, asset: str, amount: float, targetAsset: str, **kwargs
# ):
#     """BUSD Convert (USER_DATA)
#     POST /sapi/v1/asset/convert-transfer
#     https://binance-docs.github.io/apidocs/spot/en/#busd-convert-trade
#     Args:
#         clientTranId (str)
#         asset (str)
#         amount (float)
#         targetAsset (str)
#     Keyword Args:
#         accountType (str, optional)
#         recvWindow (int, optional)
#     """

#     check_required_parameters(
#         [
#             [clientTranId, "clientTranId"],
#             [asset, "asset"],
#             [amount, "amount"],
#             [targetAsset, "targetAsset"],
#         ]
#     )

#     url_path = "/sapi/v1/asset/convert-transfer"
#     payload = {
#         "clientTranId": clientTranId,
#         "asset": asset,
#         "amount": amount,
#         "targetAsset": targetAsset,
#         **kwargs,
#     }
#     return self.sign_request("POST", url_path, payload)


# def convert_history(self, startTime: int, endTime: int, **kwargs):
#     """BUSD Convert History (USER_DATA)
#     GET /sapi/v1/asset/convert-transfer/queryByPage
#     https://binance-docs.github.io/apidocs/spot/en/#busd-convert-history-user_data
#     Args:
#         startTime (int)
#         endTime (int)
#     Keyword Args:
#         tranId (int, optional)
#         clientTranId (str, optional)
#         asset (str, optional)
#         accountType (str, optional)
#         current (int, optional): Default Value: 1
#         size (int, optional): Default Value: 100; Max Value: 100
#         recvWindow (int, optional)
#     """

#     check_required_parameters([[startTime, "startTime"], [endTime, "endTime"]])

#     url_path = "/sapi/v1/asset/convert-transfer/queryByPage"
#     payload = {"startTime": startTime, "endTime": endTime, **kwargs}
#     return self.sign_request("GET", url_path, payload)



# print(api_key)
# print(api_secret)
# client = Client(api_key, api_secret)
# print(client)
# response = client.deposit_address(coin="BNB")
# print(response)