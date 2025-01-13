functions = [

    # --------------------------------------------------------------------------
    # 1) STOCK TIME SERIES
    # --------------------------------------------------------------------------

    {
        "name": "get_time_series_intraday",
        "description": (
            "Retrieve intraday time series for a given stock symbol. "
            "Corresponds to 'function=TIME_SERIES_INTRADAY' in Alpha Vantage."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "Stock symbol (e.g. 'IBM')."
                },
                "interval": {
                    "type": "string",
                    "description": "Time interval between data points (e.g. '1min', '5min', '15min', '30min', '60min').",
                    "enum": ["1min", "5min", "15min", "30min", "60min"]
                },
                "adjusted": {
                    "type": "boolean",
                    "description": "If true, the output is adjusted by historical split/dividend events.",
                    "default": False
                },
                "outputsize": {
                    "type": "string",
                    "description": "'compact' returns last 100 data points, 'full' returns entire history.",
                    "enum": ["compact", "full"],
                    "default": "compact"
                },
                "datatype": {
                    "type": "string",
                    "description": "Output format. 'json' or 'csv'.",
                    "enum": ["json", "csv"],
                    "default": "json"
                },
                "api_key": {
                    "type": "string",
                    "description": "Alpha Vantage API key.",
                    "default": "demo"
                }
            },
            "required": ["symbol", "interval"]
        },
    },
    {
        "name": "get_time_series_intraday_extended",
        "description": (
            "Retrieve historical intraday data in CSV format over 2+ years, "
            "divided into 24 'slice' segments. Corresponds to 'TIME_SERIES_INTRADAY_EXTENDED'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "Stock symbol (e.g. 'IBM')."
                },
                "interval": {
                    "type": "string",
                    "description": "Time interval (e.g. '1min', '5min', '15min', '30min', '60min').",
                    "enum": ["1min", "5min", "15min", "30min", "60min"]
                },
                "slice": {
                    "type": "string",
                    "description": (
                        "Data 'slice' to fetch (e.g. 'year1month1', 'year1month2', ... 'year2month12')."
                    )
                },
                "adjusted": {
                    "type": "boolean",
                    "description": "If true, returns adjusted intraday data.",
                    "default": False
                },
                "api_key": {
                    "type": "string",
                    "description": "Alpha Vantage API key.",
                    "default": "demo"
                }
            },
            "required": ["symbol", "interval", "slice"]
        },
    },
    {
        "name": "get_time_series_daily",
        "description": (
            "Retrieve daily time series (unadjusted) for a given stock symbol. "
            "Corresponds to 'TIME_SERIES_DAILY'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "Stock symbol (e.g. 'IBM')."
                },
                "outputsize": {
                    "type": "string",
                    "description": "'compact' returns ~100 days, 'full' returns full-length daily data.",
                    "enum": ["compact", "full"],
                    "default": "compact"
                },
                "datatype": {
                    "type": "string",
                    "description": "Output format. 'json' or 'csv'.",
                    "enum": ["json", "csv"],
                    "default": "json"
                },
                "api_key": {
                    "type": "string",
                    "description": "Alpha Vantage API key.",
                    "default": "demo"
                }
            },
            "required": ["symbol"]
        },
    },
    {
        "name": "get_time_series_daily_adjusted",
        "description": (
            "Retrieve daily time series (adjusted) for a given stock symbol. "
            "Includes split/dividend adjustments. Corresponds to 'TIME_SERIES_DAILY_ADJUSTED'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "Stock symbol (e.g. 'IBM')."
                },
                "outputsize": {
                    "type": "string",
                    "enum": ["compact", "full"],
                    "default": "compact"
                },
                "datatype": {
                    "type": "string",
                    "enum": ["json", "csv"],
                    "default": "json"
                },
                "api_key": {
                    "type": "string",
                    "default": "demo"
                }
            },
            "required": ["symbol"]
        },
    },
    {
        "name": "get_time_series_weekly",
        "description": (
            "Retrieve weekly time series (unadjusted) for a given stock symbol. "
            "Corresponds to 'TIME_SERIES_WEEKLY'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "datatype": {
                    "type": "string",
                    "enum": ["json", "csv"],
                    "default": "json"
                },
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["symbol"]
        },
    },
    {
        "name": "get_time_series_weekly_adjusted",
        "description": (
            "Retrieve weekly adjusted time series for a given stock symbol. "
            "Corresponds to 'TIME_SERIES_WEEKLY_ADJUSTED'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "datatype": {
                    "type": "string",
                    "enum": ["json", "csv"],
                    "default": "json"
                },
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["symbol"]
        },
    },
    {
        "name": "get_time_series_monthly",
        "description": (
            "Retrieve monthly time series (unadjusted) for a given stock symbol. "
            "Corresponds to 'TIME_SERIES_MONTHLY'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "datatype": {
                    "type": "string",
                    "enum": ["json", "csv"],
                    "default": "json"
                },
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["symbol"]
        },
    },
    {
        "name": "get_time_series_monthly_adjusted",
        "description": (
            "Retrieve monthly adjusted time series for a given stock symbol. "
            "Corresponds to 'TIME_SERIES_MONTHLY_ADJUSTED'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "datatype": {
                    "type": "string",
                    "enum": ["json", "csv"],
                    "default": "json"
                },
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["symbol"]
        },
    },
    {
        "name": "get_batch_stock_quotes",
        "description": (
            "Get stock quotes for multiple symbols in one request. "
            "Corresponds to 'BATCH_STOCK_QUOTES'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbols": {
                    "type": "string",
                    "description": "Comma-separated list of symbols (e.g. 'IBM,GOOG')"
                },
                "datatype": {
                    "type": "string",
                    "enum": ["json", "csv"],
                    "default": "json"
                },
                "api_key": {
                    "type": "string",
                    "default": "demo"
                }
            },
            "required": ["symbols"]
        },
    },
    {
        "name": "get_global_quote",
        "description": (
            "Return the latest trading day quote for a single stock symbol. "
            "Corresponds to 'GLOBAL_QUOTE'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "datatype": {
                    "type": "string",
                    "enum": ["json", "csv"],
                    "default": "json"
                },
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["symbol"]
        },
    },
    {
        "name": "symbol_search",
        "description": (
            "Search for best-matching symbols and companies. "
            "Corresponds to 'SYMBOL_SEARCH'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "keywords": {
                    "type": "string",
                    "description": "Company name or keyword (e.g. 'Micro')."
                },
                "datatype": {
                    "type": "string",
                    "enum": ["json", "csv"],
                    "default": "json"
                },
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["keywords"]
        },
    },

    # --------------------------------------------------------------------------
    # 2) FUNDAMENTAL DATA
    # --------------------------------------------------------------------------

    {
        "name": "get_company_overview",
        "description": (
            "Returns company overview, financial ratios, and other key fundamentals. "
            "Corresponds to 'OVERVIEW'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["symbol"]
        },
    },
    {
        "name": "get_earnings",
        "description": (
            "Returns quarterly and annual earnings (EPS) data. "
            "Corresponds to 'EARNINGS'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["symbol"]
        },
    },
    {
        "name": "get_income_statement",
        "description": (
            "Returns annual and quarterly income statements. "
            "Corresponds to 'INCOME_STATEMENT'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["symbol"]
        },
    },
    {
        "name": "get_balance_sheet",
        "description": (
            "Returns annual and quarterly balance sheets. "
            "Corresponds to 'BALANCE_SHEET'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["symbol"]
        },
    },
    {
        "name": "get_cash_flow",
        "description": (
            "Returns annual and quarterly cash flow statements. "
            "Corresponds to 'CASH_FLOW'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["symbol"]
        },
    },
    {
        "name": "get_listing_status",
        "description": (
            "Returns listing (or delisting) status of stocks. "
            "Corresponds to 'LISTING_STATUS'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "state": {
                    "type": "string",
                    "description": "'active' or 'delisted'",
                    "enum": ["active", "delisted"],
                    "default": "active"
                },
                "date": {
                    "type": "string",
                    "description": "Format: YYYY-MM-DD. Optionally used for searching by listing date."
                },
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": []
        },
    },
    {
        "name": "get_dividend_history",
        "description": (
            "Returns dividend payout history for a given stock symbol. "
            "Corresponds to 'DIVIDEND_HISTORY' in fundamental data section."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "datatype": {
                    "type": "string",
                    "enum": ["json", "csv"],
                    "default": "json"
                },
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["symbol"]
        },
    },

    # --------------------------------------------------------------------------
    # 3) FOREX
    # --------------------------------------------------------------------------

    {
        "name": "get_currency_exchange_rate",
        "description": (
            "Returns the real-time currency exchange rate for any pair. "
            "Corresponds to 'CURRENCY_EXCHANGE_RATE'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "from_currency": {"type": "string", "description": "E.g. 'USD'"},
                "to_currency": {"type": "string", "description": "E.g. 'EUR'"},
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["from_currency", "to_currency"]
        },
    },
    {
        "name": "get_fx_intraday",
        "description": (
            "Returns intraday foreign exchange (FX) data. "
            "Corresponds to 'FX_INTRADAY'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "from_symbol": {"type": "string", "description": "E.g. 'EUR'"},
                "to_symbol": {"type": "string", "description": "E.g. 'USD'"},
                "interval": {
                    "type": "string",
                    "enum": ["1min", "5min", "15min", "30min", "60min"]
                },
                "outputsize": {
                    "type": "string",
                    "enum": ["compact", "full"],
                    "default": "compact"
                },
                "datatype": {
                    "type": "string",
                    "enum": ["json", "csv"],
                    "default": "json"
                },
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["from_symbol", "to_symbol", "interval"]
        },
    },
    {
        "name": "get_fx_daily",
        "description": (
            "Returns daily FX data. Corresponds to 'FX_DAILY'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "from_symbol": {"type": "string"},
                "to_symbol": {"type": "string"},
                "outputsize": {
                    "type": "string",
                    "enum": ["compact", "full"],
                    "default": "compact"
                },
                "datatype": {
                    "type": "string",
                    "enum": ["json", "csv"],
                    "default": "json"
                },
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["from_symbol", "to_symbol"]
        },
    },
    {
        "name": "get_fx_weekly",
        "description": (
            "Returns weekly FX data. Corresponds to 'FX_WEEKLY'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "from_symbol": {"type": "string"},
                "to_symbol": {"type": "string"},
                "datatype": {
                    "type": "string",
                    "enum": ["json", "csv"],
                    "default": "json"
                },
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["from_symbol", "to_symbol"]
        },
    },
    {
        "name": "get_fx_monthly",
        "description": (
            "Returns monthly FX data. Corresponds to 'FX_MONTHLY'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "from_symbol": {"type": "string"},
                "to_symbol": {"type": "string"},
                "datatype": {
                    "type": "string",
                    "enum": ["json", "csv"],
                    "default": "json"
                },
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["from_symbol", "to_symbol"]
        },
    },

    # --------------------------------------------------------------------------
    # 4) CRYPTOCURRENCIES
    # --------------------------------------------------------------------------

    {
        "name": "get_crypto_intraday",
        "description": (
            "Returns intraday data for cryptocurrencies. "
            "Corresponds to 'CRYPTO_INTRADAY'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string", "description": "Digital currency symbol (e.g. 'BTC')."},
                "market": {"type": "string", "description": "Currency market (e.g. 'USD')."},
                "interval": {
                    "type": "string",
                    "enum": ["1min", "5min", "15min", "30min", "60min"]
                },
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["symbol", "market", "interval"]
        },
    },
    {
        "name": "get_digital_currency_daily",
        "description": (
            "Returns daily digital currency data. "
            "Corresponds to 'DIGITAL_CURRENCY_DAILY'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "market": {"type": "string"},
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["symbol", "market"]
        },
    },
    {
        "name": "get_digital_currency_weekly",
        "description": (
            "Returns weekly digital currency data. "
            "Corresponds to 'DIGITAL_CURRENCY_WEEKLY'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "market": {"type": "string"},
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["symbol", "market"]
        },
    },
    {
        "name": "get_digital_currency_monthly",
        "description": (
            "Returns monthly digital currency data. "
            "Corresponds to 'DIGITAL_CURRENCY_MONTHLY'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "market": {"type": "string"},
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": ["symbol", "market"]
        }    
    },

    # --------------------------------------------------------------------------
    # 6) SECTOR PERFORMANCE
    # --------------------------------------------------------------------------
    {
        "name": "get_sector_performance",
        "description": (
            "Returns the current and historical performance of various sectors. "
            "Corresponds to 'SECTOR'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "api_key": {"type": "string", "default": "demo"}
            },
            "required": []
        }
    }

]
