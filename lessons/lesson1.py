lesson = {
    'id': 1,
    'title': 'Tones, Greetings and Basic Expressions',
    'content': {
        'stages': [
            {
                'name': 'Tone Training',
                'type': 'tutorial',
                'title': 'Understanding Chinese Tones',
                'description': '''
Mandarin Chinese is a tonal language, which means that the pitch pattern of a syllable affects its meaning. Think of tones as the melody of the language - just as changing a musical note changes the song, 
changing a tone in Chinese changes the meaning of the word.
                ''',
                'tones': [
                    {
                        'number': '1️⃣',
                        'name': 'First Tone',
                        'description': 'High and steady pitch, like singing a single high note',
                        'color': '#4CAF50',
                        'visual_pattern': 'straight',
                        'example': {
                            'char': '妈',
                            'pinyin': 'mā',
                            'meaning': 'mother',
                            'audio_tip': 'Keep your voice steady and high',
                            'more_examples': [
                                {'char': '爸', 'pinyin': 'bā', 'meaning': 'father'},
                                {'char': '高', 'pinyin': 'gāo', 'meaning': 'tall'}
                            ]
                        }
                    },
                    {
                        'number': '2️⃣',
                        'name': 'Second Tone',
                        'description': 'Rising pitch, like asking "Really?" in English',
                        'color': '#2196F3',
                        'visual_pattern': 'rising',
                        'example': {
                            'char': '麻',
                            'pinyin': 'má',
                            'meaning': 'hemp',
                            'audio_tip': 'Your voice rises up like a question',
                            'more_examples': [
                                {'char': '来', 'pinyin': 'lái', 'meaning': 'come'},
                                {'char': '学', 'pinyin': 'xué', 'meaning': 'study'}
                            ]
                        }
                    },
                    {
                        'number': '3️⃣',
                        'name': 'Third Tone',
                        'description': 'Dips down then rises, like a valley',
                        'color': '#9C27B0',
                        'visual_pattern': 'dipping',
                        'example': {
                            'char': '马',
                            'pinyin': 'mǎ',
                            'meaning': 'horse',
                            'audio_tip': 'Your voice goes down and up',
                            'more_examples': [
                                {'char': '我', 'pinyin': 'wǒ', 'meaning': 'I/me'},
                                {'char': '你', 'pinyin': 'nǐ', 'meaning': 'you'}
                            ]
                        }
                    },
                    {
                        'number': '4️⃣',
                        'name': 'Fourth Tone',
                        'description': 'Sharp falling pitch, like giving a command',
                        'color': '#F44336',
                        'visual_pattern': 'falling',
                        'example': {
                            'char': '骂',
                            'pinyin': 'mà',
                            'meaning': 'scold',
                            'audio_tip': 'Your voice drops sharply',
                            'more_examples': [
                                {'char': '是', 'pinyin': 'shì', 'meaning': 'is/am/are'},
                                {'char': '不', 'pinyin': 'bù', 'meaning': 'no/not'}
                            ]
                        }
                    },
                    {
                        'number': '5️⃣',
                        'name': 'Neutral Tone',
                        'description': 'Light and short, like a quick tap',
                        'color': '#9E9E9E',
                        'visual_pattern': 'dot',
                        'example': {
                            'char': '的',
                            'pinyin': 'de',
                            'meaning': 'possessive particle',
                            'audio_tip': 'Pronounce it quickly and lightly',
                            'more_examples': [
                                {'char': '了', 'pinyin': 'le', 'meaning': 'particle'},
                                {'char': '吗', 'pinyin': 'ma', 'meaning': 'question particle'}
                            ]
                        }
                    }
                ],
                'tone_visualizer': {
                    'width': 300,
                    'height': 150,
                    'patterns': {
                        'straight': {'start': [0, 50], 'end': [300, 50]},
                        'rising': {'start': [0, 100], 'end': [300, 0]},
                        'dipping': {'points': [[0, 50], [150, 100], [300, 0]]},
                        'falling': {'start': [0, 0], 'end': [300, 100]},
                        'dot': {'center': [150, 50], 'radius': 3}
                    }
                },
                'interactive_elements': {
                    'play_sound': True,
                    'show_pitch_curve': True,
                    'record_practice': True,
                    'compare_with_native': True
                },
                'tone_rules': [
                    {
                        'title': 'Third Tone Change Rule',
                        'description': 'When two third tones are together, the first one changes to second tone',
                        'example': {
                            'text': '你好',
                            'pinyin': 'Nǐ hǎo → Ní hǎo',
                            'meaning': 'Hello'
                        }
                    },
                    {
                        'title': 'Neutral Tone',
                        'description': 'Some syllables are pronounced lightly without a specific tone',
                        'example': {
                            'text': '妈妈',
                            'pinyin': 'mā ma',
                            'meaning': 'Mother'
                        }
                    }
                ],
            },
            {
                'name': 'Basic Greetings',
                'type': 'learning',
                'content': '''
                <div class="learning-section">
                    <!-- General Greeting -->

                    <!-- 1. 你好 -->
                    <div class="main-expression" onclick="speakText('你好')">
                        <div class="expression-content">
                            <div class="chinese-text">你好</div>
                            <div class="expression-details">
                                <div class="pinyin">Nǐ hǎo</div>
                                <div class="meaning">Hello (General greeting)</div>
                            </div>
                        </div>
                    </div>

                    <!-- 2. 早上好 -->
                    <div class="main-expression" onclick="speakText('早上好')">
                        <div class="expression-content">
                            <div class="chinese-text">早上好</div>
                            <div class="expression-details">
                                <div class="pinyin">Zǎo shang hǎo</div>
                                <div class="meaning">Good morning</div>
                            </div>
                        </div>
                    </div>

                    <!-- 3. 下午好 -->
                    <div class="main-expression" onclick="speakText('下午好')">
                        <div class="expression-content">
                            <div class="chinese-text">下午好</div>
                            <div class="expression-details">
                                <div class="pinyin">Xià wǔ hǎo</div>
                                <div class="meaning">Good afternoon</div>
                            </div>
                        </div>
                    </div>

                    <!-- 4. 晚上好 -->
                    <div class="main-expression" onclick="speakText('晚上好')">
                        <div class="expression-content">
                            <div class="chinese-text">晚上好</div>
                            <div class="expression-details">
                                <div class="pinyin">Wǎn shang hǎo</div>
                                <div class="meaning">Good evening</div>
                            </div>
                        </div>
                    </div>

                    <!-- 5. 您好 -->
                    <div class="main-expression" onclick="speakText('您好')">
                        <div class="expression-content">
                            <div class="chinese-text">您好</div>
                            <div class="expression-details">
                                <div class="pinyin">Nín hǎo</div>
                                <div class="meaning">Hello (Polite/Formal)</div>
                            </div>
                        </div>
                    </div>

                    <!-- Usage Notes -->
                    <div class="tone-rule">
                        <div class="rule-header">
                            <span class="rule-icon">💡</span>
                            <span class="rule-title">Important Notes</span>
                        </div>
                        <ul class="usage-notes">
                            <li>你好 (Nǐ hǎo) is the most common, everyday greeting</li>
                            <li>您好 (Nín hǎo) is formal/respectful, used with elders or in business</li>
                            <li>Time-specific greetings (早上好, 下午好, 晚上好) show attention to detail</li>
                        </ul>
                    </div>

                    <div class="usage-examples">
                        <h4>Common Usage</h4>
                        <!-- Casual Situations -->
                        <div class="usage-item" onclick="speakText('你好！')">
                            <div class="usage-chinese">你好！</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">Nǐ hǎo!</div>
                                <div class="usage-meaning">Hello!</div>
                            </div>
                        </div>

                        <!-- Formal Introduction -->
                        <div class="usage-item" onclick="speakText('您好，我是王老师。')">
                            <div class="usage-chinese">您好，我是王老师。</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">Nín hǎo, wǒ shì Wáng lǎoshī.</div>
                                <div class="usage-meaning">Hello, I am Teacher Wang.</div>
                            </div>
                        </div>

                        <!-- Morning Greeting -->
                        <div class="usage-item" onclick="speakText('早上好！今天天气真好。')">
                            <div class="usage-chinese">早上好！今天天气真好。</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">Zǎo shang hǎo! Jīntiān tiānqì zhēn hǎo.</div>
                                <div class="usage-meaning">Good morning! The weather is nice today.</div>
                            </div>
                        </div>
                    </div>
                </div>
                '''
            },
            {
                'name': 'Thank You Power',
                'type': 'learning',
                'content': '''
                <div class="learning-section">

                    <!-- 1. Basic Thank You -->
                    <div class="main-expression" onclick="speakText('谢谢')">
                        <div class="expression-content">
                            <div class="chinese-text">谢谢</div>
                            <div class="expression-details">
                                <div class="pinyin">Xiè xie</div>
                                <div class="meaning">Thank you (Basic/Common)</div>
                            </div>
                        </div>
                    </div>

                    <!-- 2. Polite Thank You -->
                    <div class="main-expression" onclick="speakText('谢谢您')">
                        <div class="expression-content">
                            <div class="chinese-text">谢谢您</div>
                            <div class="expression-details">
                                <div class="pinyin">Xiè xie nín</div>
                                <div class="meaning">Thank you (Polite/Formal)</div>
                            </div>
                        </div>
                    </div>

                    <!-- 3. Thank You Very Much -->
                    <div class="main-expression" onclick="speakText('非常感谢')">
                        <div class="expression-content">
                            <div class="chinese-text">非常感谢</div>
                            <div class="expression-details">
                                <div class="pinyin">Fēi cháng gǎn xiè</div>
                                <div class="meaning">Thank you very much</div>
                            </div>
                        </div>
                    </div>

                    <!-- 4. Many Thanks -->
                    <div class="main-expression" onclick="speakText('多谢')">
                        <div class="expression-content">
                            <div class="chinese-text">多谢</div>
                            <div class="expression-details">
                                <div class="pinyin">Duō xiè</div>
                                <div class="meaning">Many thanks</div>
                            </div>
                        </div>
                    </div>

                    <!-- 5. Thanks for Your Help -->
                    <div class="main-expression" onclick="speakText('谢谢你的帮助')">
                        <div class="expression-content">
                            <div class="chinese-text">谢谢你的帮助</div>
                            <div class="expression-details">
                                <div class="pinyin">Xiè xie nǐ de bāng zhù</div>
                                <div class="meaning">Thank you for your help</div>
                            </div>
                        </div>
                    </div>

                    <div class="tone-rule">
                        <div class="rule-header">
                            <span class="rule-icon">💡</span>
                            <span class="rule-title">Important Notes</span>
                        </div>
                        <ul class="usage-notes">
                            <li>谢谢 (Xiè xie) is the most common way to say thank you</li>
                            <li>谢谢您 (Xiè xie nín) is formal, used with elders or in business</li>
                            <li>非常感谢 (Fēi cháng gǎn xiè) expresses deeper gratitude</li>
                            <li>多谢 (Duō xiè) is slightly more casual</li>
                        </ul>
                    </div>

                    <div class="usage-examples">
                        <h4>Common Usage</h4>
                        <!-- Basic Thanks -->
                        <div class="usage-item" onclick="speakText('谢谢你！')">
                            <div class="usage-chinese">谢谢你！</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">Xiè xie nǐ!</div>
                                <div class="usage-meaning">Thank you!</div>
                            </div>
                        </div>

                        <!-- Formal Thanks -->
                        <div class="usage-item" onclick="speakText('非常感谢您的帮助。')">
                            <div class="usage-chinese">非常感谢您的帮助。</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">Fēi cháng gǎn xiè nín de bāng zhù.</div>
                                <div class="usage-meaning">Thank you very much for your help. (Formal)</div>
                            </div>
                        </div>

                        <!-- Thanks with Context -->
                        <div class="usage-item" onclick="speakText('多谢你的关心。')">
                            <div class="usage-chinese">多谢你的关心。</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">Duō xiè nǐ de guān xīn.</div>
                                <div class="usage-meaning">Thanks for your concern.</div>
                            </div>
                        </div>

                        <!-- Response to Service -->
                        <div class="usage-item" onclick="speakText('谢谢您的服务。')">
                            <div class="usage-chinese">谢谢您的服务。</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">Xiè xie nín de fú wù.</div>
                                <div class="usage-meaning">Thank you for your service.</div>
                            </div>
                        </div>
                    </div>
                </div>
                '''
            }
        ],
        'tips': '''
            <div class="study-tips">
                <div class="section-title">
                    <div class="title-with-icon">
                        <span class="icon">💡</span>
                        <span>Study Tips</span>
                    </div>
                </div>
                <div class="tip-block">
                    <h4>Listen Carefully</h4>
                    <p>Pay attention to native speakers' tone patterns and try to mimic them</p>
                </div>

                <div class="tip-block">
                    <h4>Practice Daily</h4>
                    <p>Spend a few minutes each day practicing the tones with simple words</p>
                </div>

                <div class="tip-block">
                    <h4>Record Yourself</h4>
                    <p>Compare your pronunciation with native speakers to improve accuracy</p>
                </div>

                <div class="tip-block">
                    <h4>Start Simple</h4>
                    <p>Master single-syllable words before moving on to longer phrases</p>
                </div>
            </div>
        ''',
        'mistakes': '''
            <div class="study-tips warning">
                <div class="tip-block">
                    <h4>Tone Consistency</h4>
                    <p>Don't change tones randomly - each character has a specific tone</p>
                </div>

                <div class="tip-block">
                    <h4>Third Tone</h4>
                    <p>Make sure to dip down before rising in third tone words</p>
                </div>

                <div class="tip-block">
                    <h4>Neutral Tone</h4>
                    <p>Don't stress neutral tone syllables too much</p>
                </div>

                <div class="tip-block">
                    <h4>Tone Changes</h4>
                    <p>Watch out for tone changes in combinations (like 不 and 一)</p>
                </div>
            </div>
        '''
    }
}