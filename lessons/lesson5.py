lesson = {
    'id': 5,
    'title': 'Food and Drinks',
    'icon': '🍜',  # Using emoji as icon until we have a custom one
    'content': {
        'stages': [
            {
                'name': 'Basic Foods',
                'type': 'learning',
                'icon': '🍚',
                'subtitle': 'Learn essential food vocabulary',
    'content': '''
                    <div class="learning-section">
                        <div class="section-intro">
                            <p>Food is an essential part of Chinese culture. Learning basic food vocabulary will help you 
                            navigate restaurants, markets, and social situations with confidence.</p>
                        </div>

                        <!-- Staple Foods -->
                        <div class="main-expression" onclick="speakText('米饭')">
                            <div class="expression-content">
                                <div class="chinese-text">米饭</div>
                                <div class="expression-details">
                                    <div class="pinyin">mǐfàn</div>
                                    <div class="meaning">rice</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('面条')">
                            <div class="expression-content">
                                <div class="chinese-text">面条</div>
                                <div class="expression-details">
                                    <div class="pinyin">miàntiáo</div>
                                    <div class="meaning">noodles</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('饺子')">
                            <div class="expression-content">
                                <div class="chinese-text">饺子</div>
                                <div class="expression-details">
                                    <div class="pinyin">jiǎozi</div>
                                    <div class="meaning">dumplings</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('包子')">
                            <div class="expression-content">
                                <div class="chinese-text">包子</div>
                                <div class="expression-details">
                                    <div class="pinyin">bāozi</div>
                                    <div class="meaning">steamed buns</div>
                                </div>
                            </div>
                        </div>

                        <!-- Drinks -->
                        <div class="main-expression" onclick="speakText('水')">
                            <div class="expression-content">
                                <div class="chinese-text">水</div>
                                <div class="expression-details">
                                    <div class="pinyin">shuǐ</div>
                                    <div class="meaning">water</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('茶')">
                            <div class="expression-content">
                                <div class="chinese-text">茶</div>
                                <div class="expression-details">
                                    <div class="pinyin">chá</div>
                                    <div class="meaning">tea</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('咖啡')">
                            <div class="expression-content">
                                <div class="chinese-text">咖啡</div>
                                <div class="expression-details">
                                    <div class="pinyin">kāfēi</div>
                                    <div class="meaning">coffee</div>
                                </div>
                            </div>
                        </div>

                        <!-- Common Ingredients -->
                        <div class="main-expression" onclick="speakText('鸡肉')">
                            <div class="expression-content">
                                <div class="chinese-text">鸡肉</div>
                                <div class="expression-details">
                                    <div class="pinyin">jīròu</div>
                                    <div class="meaning">chicken</div>
                                </div>
                            </div>
                        </div>

                        <div class="main-expression" onclick="speakText('牛肉')">
                            <div class="expression-content">
                                <div class="chinese-text">牛肉</div>
                                <div class="expression-details">
                                    <div class="pinyin">niúròu</div>
                                    <div class="meaning">beef</div>
                                </div>
                            </div>
                        </div>

                        <!-- Important Notes -->
                        <div class="tone-rule">
                            <div class="rule-header">
                                <span class="rule-icon">💡</span>
                                <span class="rule-title">Important Notes</span>
                            </div>
                            <ul class="usage-notes">
                                <li>Use 吃 for eating and 喝 for drinking</li>
                                <li>Remember to use measure words with countable foods</li>
                                <li>Meals often end with 饭 (fàn)</li>
                                <li>Food terms rarely use 的 in simple forms</li>
                            </ul>
                        </div>
                    </div>
                '''
            },
            {
                'name': 'Common Usage',
                'type': 'examples',
                'content': '''
                    <div class="usage-examples">
                        <!-- Basic Expressions -->
                        <div class="usage-item" onclick="speakText('我喜欢吃米饭')">
                            <div class="usage-chinese">我喜欢吃米饭</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">wǒ xǐhuan chī mǐfàn</div>
                                <div class="usage-meaning">I like to eat rice</div>
                            </div>
                        </div>

                        <div class="usage-item" onclick="speakText('这个面条很好吃')">
                            <div class="usage-chinese">这个面条很好吃</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">zhège miàntiáo hěn hǎochī</div>
                                <div class="usage-meaning">These noodles are delicious</div>
                            </div>
                        </div>

                        <!-- Restaurant Phrases -->
                        <div class="usage-item" onclick="speakText('我要一碗米饭')">
                            <div class="usage-chinese">我要一碗米饭</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">wǒ yào yì wǎn mǐfàn</div>
                                <div class="usage-meaning">I want a bowl of rice</div>
                            </div>
                        </div>

                        <div class="usage-item" onclick="speakText('请给我一杯茶')">
                            <div class="usage-chinese">请给我一杯茶</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">qǐng gěi wǒ yì bēi chá</div>
                                <div class="usage-meaning">Please give me a cup of tea</div>
                            </div>
                        </div>

                        <!-- Preferences -->
                        <div class="usage-item" onclick="speakText('我不吃牛肉')">
                            <div class="usage-chinese">我不吃牛肉</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">wǒ bù chī niúròu</div>
                                <div class="usage-meaning">I don't eat beef</div>
                            </div>
                        </div>

                        <div class="usage-item" onclick="speakText('这个饺子很辣')">
                            <div class="usage-chinese">这个饺子很辣</div>
                            <div class="usage-details">
                                <div class="usage-pinyin">zhège jiǎozi hěn là</div>
                                <div class="usage-meaning">This dumpling is very spicy</div>
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
                    <h4>Basic Verbs</h4>
                    <p>Use 吃 for eating, 喝 for drinking</p>
                </div>

                <div class="tip-block">
                    <h4>Measure Words</h4>
                    <p>碗 for rice/noodles, 杯 for drinks, 个 for items</p>
                </div>

                <div class="tip-block">
                    <h4>Common Patterns</h4>
                    <p>Practice with: 我想吃/喝..., 请给我..., 这个...很好吃</p>
                </div>

                <div class="tip-block">
                    <h4>Restaurant Tips</h4>
                    <p>Learn to order with 我要... and 请给我...</p>
                </div>
            </div>
''',
    'mistakes': '''
            <div class="study-tips warning">
                <div class="tip-block">
                    <h4>Word Order</h4>
                    <p>Don't use 的 with simple food items</p>
                </div>

                <div class="tip-block">
                    <h4>Measure Words</h4>
                    <p>Don't forget measure words for countable foods</p>
                </div>

                <div class="tip-block">
                    <h4>Verb Usage</h4>
                    <p>Don't mix up 吃 and 喝 - they're not interchangeable</p>
                </div>

                <div class="tip-block">
                    <h4>Ordering</h4>
                    <p>Don't forget to use polite forms when ordering (请...)</p>
                </div>
            </div>
        '''
    }
} 