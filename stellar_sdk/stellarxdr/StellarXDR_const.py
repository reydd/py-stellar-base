# Generated by xdrgen.py from ../xdr/ on Wed Jun 19 10:37:57 2019
KEY_TYPE_ED25519 = 0
KEY_TYPE_PRE_AUTH_TX = 1
KEY_TYPE_HASH_X = 2
CryptoKeyType = {
    0 : 'KEY_TYPE_ED25519',
    1 : 'KEY_TYPE_PRE_AUTH_TX',
    2 : 'KEY_TYPE_HASH_X',
}
PUBLIC_KEY_TYPE_ED25519 = KEY_TYPE_ED25519
PublicKeyType = {
    KEY_TYPE_ED25519 : 'PUBLIC_KEY_TYPE_ED25519',
}
SIGNER_KEY_TYPE_ED25519 = KEY_TYPE_ED25519
SIGNER_KEY_TYPE_PRE_AUTH_TX = KEY_TYPE_PRE_AUTH_TX
SIGNER_KEY_TYPE_HASH_X = KEY_TYPE_HASH_X
SignerKeyType = {
    KEY_TYPE_ED25519 : 'SIGNER_KEY_TYPE_ED25519',
    KEY_TYPE_PRE_AUTH_TX : 'SIGNER_KEY_TYPE_PRE_AUTH_TX',
    KEY_TYPE_HASH_X : 'SIGNER_KEY_TYPE_HASH_X',
}
SCP_ST_PREPARE = 0
SCP_ST_CONFIRM = 1
SCP_ST_EXTERNALIZE = 2
SCP_ST_NOMINATE = 3
SCPStatementType = {
    0 : 'SCP_ST_PREPARE',
    1 : 'SCP_ST_CONFIRM',
    2 : 'SCP_ST_EXTERNALIZE',
    3 : 'SCP_ST_NOMINATE',
}
STELLAR_VALUE_BASIC = 0
STELLAR_VALUE_SIGNED = 1
StellarValueType = {
    0 : 'STELLAR_VALUE_BASIC',
    1 : 'STELLAR_VALUE_SIGNED',
}
LEDGER_UPGRADE_VERSION = 1
LEDGER_UPGRADE_BASE_FEE = 2
LEDGER_UPGRADE_MAX_TX_SET_SIZE = 3
LEDGER_UPGRADE_BASE_RESERVE = 4
LedgerUpgradeType = {
    1 : 'LEDGER_UPGRADE_VERSION',
    2 : 'LEDGER_UPGRADE_BASE_FEE',
    3 : 'LEDGER_UPGRADE_MAX_TX_SET_SIZE',
    4 : 'LEDGER_UPGRADE_BASE_RESERVE',
}
METAENTRY = -1
LIVEENTRY = 0
DEADENTRY = 1
INITENTRY = 2
BucketEntryType = {
    -1 : 'METAENTRY',
    0 : 'LIVEENTRY',
    1 : 'DEADENTRY',
    2 : 'INITENTRY',
}
LEDGER_ENTRY_CREATED = 0
LEDGER_ENTRY_UPDATED = 1
LEDGER_ENTRY_REMOVED = 2
LEDGER_ENTRY_STATE = 3
LedgerEntryChangeType = {
    0 : 'LEDGER_ENTRY_CREATED',
    1 : 'LEDGER_ENTRY_UPDATED',
    2 : 'LEDGER_ENTRY_REMOVED',
    3 : 'LEDGER_ENTRY_STATE',
}
ASSET_TYPE_NATIVE = 0
ASSET_TYPE_CREDIT_ALPHANUM4 = 1
ASSET_TYPE_CREDIT_ALPHANUM12 = 2
AssetType = {
    0 : 'ASSET_TYPE_NATIVE',
    1 : 'ASSET_TYPE_CREDIT_ALPHANUM4',
    2 : 'ASSET_TYPE_CREDIT_ALPHANUM12',
}
THRESHOLD_MASTER_WEIGHT = 0
THRESHOLD_LOW = 1
THRESHOLD_MED = 2
THRESHOLD_HIGH = 3
ThresholdIndexes = {
    0 : 'THRESHOLD_MASTER_WEIGHT',
    1 : 'THRESHOLD_LOW',
    2 : 'THRESHOLD_MED',
    3 : 'THRESHOLD_HIGH',
}
ACCOUNT = 0
TRUSTLINE = 1
OFFER = 2
DATA = 3
LedgerEntryType = {
    0 : 'ACCOUNT',
    1 : 'TRUSTLINE',
    2 : 'OFFER',
    3 : 'DATA',
}
AUTH_REQUIRED_FLAG = 0x1
AUTH_REVOCABLE_FLAG = 0x2
AUTH_IMMUTABLE_FLAG = 0x4
AccountFlags = {
    0x1 : 'AUTH_REQUIRED_FLAG',
    0x2 : 'AUTH_REVOCABLE_FLAG',
    0x4 : 'AUTH_IMMUTABLE_FLAG',
}
MASK_ACCOUNT_FLAGS = 0x7
AUTHORIZED_FLAG = 1
TrustLineFlags = {
    1 : 'AUTHORIZED_FLAG',
}
MASK_TRUSTLINE_FLAGS = 1
PASSIVE_FLAG = 1
OfferEntryFlags = {
    1 : 'PASSIVE_FLAG',
}
MASK_OFFERENTRY_FLAGS = 1
ENVELOPE_TYPE_SCP = 1
ENVELOPE_TYPE_TX = 2
ENVELOPE_TYPE_AUTH = 3
ENVELOPE_TYPE_SCPVALUE = 4
EnvelopeType = {
    1 : 'ENVELOPE_TYPE_SCP',
    2 : 'ENVELOPE_TYPE_TX',
    3 : 'ENVELOPE_TYPE_AUTH',
    4 : 'ENVELOPE_TYPE_SCPVALUE',
}
CREATE_ACCOUNT = 0
PAYMENT = 1
PATH_PAYMENT = 2
MANAGE_SELL_OFFER = 3
CREATE_PASSIVE_SELL_OFFER = 4
SET_OPTIONS = 5
CHANGE_TRUST = 6
ALLOW_TRUST = 7
ACCOUNT_MERGE = 8
INFLATION = 9
MANAGE_DATA = 10
BUMP_SEQUENCE = 11
MANAGE_BUY_OFFER = 12
OperationType = {
    0 : 'CREATE_ACCOUNT',
    1 : 'PAYMENT',
    2 : 'PATH_PAYMENT',
    3 : 'MANAGE_SELL_OFFER',
    4 : 'CREATE_PASSIVE_SELL_OFFER',
    5 : 'SET_OPTIONS',
    6 : 'CHANGE_TRUST',
    7 : 'ALLOW_TRUST',
    8 : 'ACCOUNT_MERGE',
    9 : 'INFLATION',
    10 : 'MANAGE_DATA',
    11 : 'BUMP_SEQUENCE',
    12 : 'MANAGE_BUY_OFFER',
}
MEMO_NONE = 0
MEMO_TEXT = 1
MEMO_ID = 2
MEMO_HASH = 3
MEMO_RETURN = 4
MemoType = {
    0 : 'MEMO_NONE',
    1 : 'MEMO_TEXT',
    2 : 'MEMO_ID',
    3 : 'MEMO_HASH',
    4 : 'MEMO_RETURN',
}
MAX_OPS_PER_TX = 100
CREATE_ACCOUNT_SUCCESS = 0
CREATE_ACCOUNT_MALFORMED = -1
CREATE_ACCOUNT_UNDERFUNDED = -2
CREATE_ACCOUNT_LOW_RESERVE = -3
CREATE_ACCOUNT_ALREADY_EXIST = -4
CreateAccountResultCode = {
    0 : 'CREATE_ACCOUNT_SUCCESS',
    -1 : 'CREATE_ACCOUNT_MALFORMED',
    -2 : 'CREATE_ACCOUNT_UNDERFUNDED',
    -3 : 'CREATE_ACCOUNT_LOW_RESERVE',
    -4 : 'CREATE_ACCOUNT_ALREADY_EXIST',
}
PAYMENT_SUCCESS = 0
PAYMENT_MALFORMED = -1
PAYMENT_UNDERFUNDED = -2
PAYMENT_SRC_NO_TRUST = -3
PAYMENT_SRC_NOT_AUTHORIZED = -4
PAYMENT_NO_DESTINATION = -5
PAYMENT_NO_TRUST = -6
PAYMENT_NOT_AUTHORIZED = -7
PAYMENT_LINE_FULL = -8
PAYMENT_NO_ISSUER = -9
PaymentResultCode = {
    0 : 'PAYMENT_SUCCESS',
    -1 : 'PAYMENT_MALFORMED',
    -2 : 'PAYMENT_UNDERFUNDED',
    -3 : 'PAYMENT_SRC_NO_TRUST',
    -4 : 'PAYMENT_SRC_NOT_AUTHORIZED',
    -5 : 'PAYMENT_NO_DESTINATION',
    -6 : 'PAYMENT_NO_TRUST',
    -7 : 'PAYMENT_NOT_AUTHORIZED',
    -8 : 'PAYMENT_LINE_FULL',
    -9 : 'PAYMENT_NO_ISSUER',
}
PATH_PAYMENT_SUCCESS = 0
PATH_PAYMENT_MALFORMED = -1
PATH_PAYMENT_UNDERFUNDED = -2
PATH_PAYMENT_SRC_NO_TRUST = -3
PATH_PAYMENT_SRC_NOT_AUTHORIZED = -4
PATH_PAYMENT_NO_DESTINATION = -5
PATH_PAYMENT_NO_TRUST = -6
PATH_PAYMENT_NOT_AUTHORIZED = -7
PATH_PAYMENT_LINE_FULL = -8
PATH_PAYMENT_NO_ISSUER = -9
PATH_PAYMENT_TOO_FEW_OFFERS = -10
PATH_PAYMENT_OFFER_CROSS_SELF = -11
PATH_PAYMENT_OVER_SENDMAX = -12
PathPaymentResultCode = {
    0 : 'PATH_PAYMENT_SUCCESS',
    -1 : 'PATH_PAYMENT_MALFORMED',
    -2 : 'PATH_PAYMENT_UNDERFUNDED',
    -3 : 'PATH_PAYMENT_SRC_NO_TRUST',
    -4 : 'PATH_PAYMENT_SRC_NOT_AUTHORIZED',
    -5 : 'PATH_PAYMENT_NO_DESTINATION',
    -6 : 'PATH_PAYMENT_NO_TRUST',
    -7 : 'PATH_PAYMENT_NOT_AUTHORIZED',
    -8 : 'PATH_PAYMENT_LINE_FULL',
    -9 : 'PATH_PAYMENT_NO_ISSUER',
    -10 : 'PATH_PAYMENT_TOO_FEW_OFFERS',
    -11 : 'PATH_PAYMENT_OFFER_CROSS_SELF',
    -12 : 'PATH_PAYMENT_OVER_SENDMAX',
}
MANAGE_SELL_OFFER_SUCCESS = 0
MANAGE_SELL_OFFER_MALFORMED = -1
MANAGE_SELL_OFFER_SELL_NO_TRUST = -2
MANAGE_SELL_OFFER_BUY_NO_TRUST = -3
MANAGE_SELL_OFFER_SELL_NOT_AUTHORIZED = -4
MANAGE_SELL_OFFER_BUY_NOT_AUTHORIZED = -5
MANAGE_SELL_OFFER_LINE_FULL = -6
MANAGE_SELL_OFFER_UNDERFUNDED = -7
MANAGE_SELL_OFFER_CROSS_SELF = -8
MANAGE_SELL_OFFER_SELL_NO_ISSUER = -9
MANAGE_SELL_OFFER_BUY_NO_ISSUER = -10
MANAGE_SELL_OFFER_NOT_FOUND = -11
MANAGE_SELL_OFFER_LOW_RESERVE = -12
ManageSellOfferResultCode = {
    0 : 'MANAGE_SELL_OFFER_SUCCESS',
    -1 : 'MANAGE_SELL_OFFER_MALFORMED',
    -2 : 'MANAGE_SELL_OFFER_SELL_NO_TRUST',
    -3 : 'MANAGE_SELL_OFFER_BUY_NO_TRUST',
    -4 : 'MANAGE_SELL_OFFER_SELL_NOT_AUTHORIZED',
    -5 : 'MANAGE_SELL_OFFER_BUY_NOT_AUTHORIZED',
    -6 : 'MANAGE_SELL_OFFER_LINE_FULL',
    -7 : 'MANAGE_SELL_OFFER_UNDERFUNDED',
    -8 : 'MANAGE_SELL_OFFER_CROSS_SELF',
    -9 : 'MANAGE_SELL_OFFER_SELL_NO_ISSUER',
    -10 : 'MANAGE_SELL_OFFER_BUY_NO_ISSUER',
    -11 : 'MANAGE_SELL_OFFER_NOT_FOUND',
    -12 : 'MANAGE_SELL_OFFER_LOW_RESERVE',
}
MANAGE_OFFER_CREATED = 0
MANAGE_OFFER_UPDATED = 1
MANAGE_OFFER_DELETED = 2
ManageOfferEffect = {
    0 : 'MANAGE_OFFER_CREATED',
    1 : 'MANAGE_OFFER_UPDATED',
    2 : 'MANAGE_OFFER_DELETED',
}
MANAGE_BUY_OFFER_SUCCESS = 0
MANAGE_BUY_OFFER_MALFORMED = -1
MANAGE_BUY_OFFER_SELL_NO_TRUST = -2
MANAGE_BUY_OFFER_BUY_NO_TRUST = -3
MANAGE_BUY_OFFER_SELL_NOT_AUTHORIZED = -4
MANAGE_BUY_OFFER_BUY_NOT_AUTHORIZED = -5
MANAGE_BUY_OFFER_LINE_FULL = -6
MANAGE_BUY_OFFER_UNDERFUNDED = -7
MANAGE_BUY_OFFER_CROSS_SELF = -8
MANAGE_BUY_OFFER_SELL_NO_ISSUER = -9
MANAGE_BUY_OFFER_BUY_NO_ISSUER = -10
MANAGE_BUY_OFFER_NOT_FOUND = -11
MANAGE_BUY_OFFER_LOW_RESERVE = -12
ManageBuyOfferResultCode = {
    0 : 'MANAGE_BUY_OFFER_SUCCESS',
    -1 : 'MANAGE_BUY_OFFER_MALFORMED',
    -2 : 'MANAGE_BUY_OFFER_SELL_NO_TRUST',
    -3 : 'MANAGE_BUY_OFFER_BUY_NO_TRUST',
    -4 : 'MANAGE_BUY_OFFER_SELL_NOT_AUTHORIZED',
    -5 : 'MANAGE_BUY_OFFER_BUY_NOT_AUTHORIZED',
    -6 : 'MANAGE_BUY_OFFER_LINE_FULL',
    -7 : 'MANAGE_BUY_OFFER_UNDERFUNDED',
    -8 : 'MANAGE_BUY_OFFER_CROSS_SELF',
    -9 : 'MANAGE_BUY_OFFER_SELL_NO_ISSUER',
    -10 : 'MANAGE_BUY_OFFER_BUY_NO_ISSUER',
    -11 : 'MANAGE_BUY_OFFER_NOT_FOUND',
    -12 : 'MANAGE_BUY_OFFER_LOW_RESERVE',
}
SET_OPTIONS_SUCCESS = 0
SET_OPTIONS_LOW_RESERVE = -1
SET_OPTIONS_TOO_MANY_SIGNERS = -2
SET_OPTIONS_BAD_FLAGS = -3
SET_OPTIONS_INVALID_INFLATION = -4
SET_OPTIONS_CANT_CHANGE = -5
SET_OPTIONS_UNKNOWN_FLAG = -6
SET_OPTIONS_THRESHOLD_OUT_OF_RANGE = -7
SET_OPTIONS_BAD_SIGNER = -8
SET_OPTIONS_INVALID_HOME_DOMAIN = -9
SetOptionsResultCode = {
    0 : 'SET_OPTIONS_SUCCESS',
    -1 : 'SET_OPTIONS_LOW_RESERVE',
    -2 : 'SET_OPTIONS_TOO_MANY_SIGNERS',
    -3 : 'SET_OPTIONS_BAD_FLAGS',
    -4 : 'SET_OPTIONS_INVALID_INFLATION',
    -5 : 'SET_OPTIONS_CANT_CHANGE',
    -6 : 'SET_OPTIONS_UNKNOWN_FLAG',
    -7 : 'SET_OPTIONS_THRESHOLD_OUT_OF_RANGE',
    -8 : 'SET_OPTIONS_BAD_SIGNER',
    -9 : 'SET_OPTIONS_INVALID_HOME_DOMAIN',
}
CHANGE_TRUST_SUCCESS = 0
CHANGE_TRUST_MALFORMED = -1
CHANGE_TRUST_NO_ISSUER = -2
CHANGE_TRUST_INVALID_LIMIT = -3
CHANGE_TRUST_LOW_RESERVE = -4
CHANGE_TRUST_SELF_NOT_ALLOWED = -5
ChangeTrustResultCode = {
    0 : 'CHANGE_TRUST_SUCCESS',
    -1 : 'CHANGE_TRUST_MALFORMED',
    -2 : 'CHANGE_TRUST_NO_ISSUER',
    -3 : 'CHANGE_TRUST_INVALID_LIMIT',
    -4 : 'CHANGE_TRUST_LOW_RESERVE',
    -5 : 'CHANGE_TRUST_SELF_NOT_ALLOWED',
}
ALLOW_TRUST_SUCCESS = 0
ALLOW_TRUST_MALFORMED = -1
ALLOW_TRUST_NO_TRUST_LINE = -2
ALLOW_TRUST_TRUST_NOT_REQUIRED = -3
ALLOW_TRUST_CANT_REVOKE = -4
ALLOW_TRUST_SELF_NOT_ALLOWED = -5
AllowTrustResultCode = {
    0 : 'ALLOW_TRUST_SUCCESS',
    -1 : 'ALLOW_TRUST_MALFORMED',
    -2 : 'ALLOW_TRUST_NO_TRUST_LINE',
    -3 : 'ALLOW_TRUST_TRUST_NOT_REQUIRED',
    -4 : 'ALLOW_TRUST_CANT_REVOKE',
    -5 : 'ALLOW_TRUST_SELF_NOT_ALLOWED',
}
ACCOUNT_MERGE_SUCCESS = 0
ACCOUNT_MERGE_MALFORMED = -1
ACCOUNT_MERGE_NO_ACCOUNT = -2
ACCOUNT_MERGE_IMMUTABLE_SET = -3
ACCOUNT_MERGE_HAS_SUB_ENTRIES = -4
ACCOUNT_MERGE_SEQNUM_TOO_FAR = -5
ACCOUNT_MERGE_DEST_FULL = -6
AccountMergeResultCode = {
    0 : 'ACCOUNT_MERGE_SUCCESS',
    -1 : 'ACCOUNT_MERGE_MALFORMED',
    -2 : 'ACCOUNT_MERGE_NO_ACCOUNT',
    -3 : 'ACCOUNT_MERGE_IMMUTABLE_SET',
    -4 : 'ACCOUNT_MERGE_HAS_SUB_ENTRIES',
    -5 : 'ACCOUNT_MERGE_SEQNUM_TOO_FAR',
    -6 : 'ACCOUNT_MERGE_DEST_FULL',
}
INFLATION_SUCCESS = 0
INFLATION_NOT_TIME = -1
InflationResultCode = {
    0 : 'INFLATION_SUCCESS',
    -1 : 'INFLATION_NOT_TIME',
}
MANAGE_DATA_SUCCESS = 0
MANAGE_DATA_NOT_SUPPORTED_YET = -1
MANAGE_DATA_NAME_NOT_FOUND = -2
MANAGE_DATA_LOW_RESERVE = -3
MANAGE_DATA_INVALID_NAME = -4
ManageDataResultCode = {
    0 : 'MANAGE_DATA_SUCCESS',
    -1 : 'MANAGE_DATA_NOT_SUPPORTED_YET',
    -2 : 'MANAGE_DATA_NAME_NOT_FOUND',
    -3 : 'MANAGE_DATA_LOW_RESERVE',
    -4 : 'MANAGE_DATA_INVALID_NAME',
}
BUMP_SEQUENCE_SUCCESS = 0
BUMP_SEQUENCE_BAD_SEQ = -1
BumpSequenceResultCode = {
    0 : 'BUMP_SEQUENCE_SUCCESS',
    -1 : 'BUMP_SEQUENCE_BAD_SEQ',
}
opINNER = 0
opBAD_AUTH = -1
opNO_ACCOUNT = -2
opNOT_SUPPORTED = -3
opTOO_MANY_SUBENTRIES = -4
opEXCEEDED_WORK_LIMIT = -5
OperationResultCode = {
    0 : 'opINNER',
    -1 : 'opBAD_AUTH',
    -2 : 'opNO_ACCOUNT',
    -3 : 'opNOT_SUPPORTED',
    -4 : 'opTOO_MANY_SUBENTRIES',
    -5 : 'opEXCEEDED_WORK_LIMIT',
}
txSUCCESS = 0
txFAILED = -1
txTOO_EARLY = -2
txTOO_LATE = -3
txMISSING_OPERATION = -4
txBAD_SEQ = -5
txBAD_AUTH = -6
txINSUFFICIENT_BALANCE = -7
txNO_ACCOUNT = -8
txINSUFFICIENT_FEE = -9
txBAD_AUTH_EXTRA = -10
txINTERNAL_ERROR = -11
TransactionResultCode = {
    0 : 'txSUCCESS',
    -1 : 'txFAILED',
    -2 : 'txTOO_EARLY',
    -3 : 'txTOO_LATE',
    -4 : 'txMISSING_OPERATION',
    -5 : 'txBAD_SEQ',
    -6 : 'txBAD_AUTH',
    -7 : 'txINSUFFICIENT_BALANCE',
    -8 : 'txNO_ACCOUNT',
    -9 : 'txINSUFFICIENT_FEE',
    -10 : 'txBAD_AUTH_EXTRA',
    -11 : 'txINTERNAL_ERROR',
}
ERR_MISC = 0
ERR_DATA = 1
ERR_CONF = 2
ERR_AUTH = 3
ERR_LOAD = 4
ErrorCode = {
    0 : 'ERR_MISC',
    1 : 'ERR_DATA',
    2 : 'ERR_CONF',
    3 : 'ERR_AUTH',
    4 : 'ERR_LOAD',
}
IPv4 = 0
IPv6 = 1
IPAddrType = {
    0 : 'IPv4',
    1 : 'IPv6',
}
ERROR_MSG = 0
AUTH = 2
DONT_HAVE = 3
GET_PEERS = 4
PEERS = 5
GET_TX_SET = 6
TX_SET = 7
TRANSACTION = 8
GET_SCP_QUORUMSET = 9
SCP_QUORUMSET = 10
SCP_MESSAGE = 11
GET_SCP_STATE = 12
HELLO = 13
MessageType = {
    0 : 'ERROR_MSG',
    2 : 'AUTH',
    3 : 'DONT_HAVE',
    4 : 'GET_PEERS',
    5 : 'PEERS',
    6 : 'GET_TX_SET',
    7 : 'TX_SET',
    8 : 'TRANSACTION',
    9 : 'GET_SCP_QUORUMSET',
    10 : 'SCP_QUORUMSET',
    11 : 'SCP_MESSAGE',
    12 : 'GET_SCP_STATE',
    13 : 'HELLO',
}
